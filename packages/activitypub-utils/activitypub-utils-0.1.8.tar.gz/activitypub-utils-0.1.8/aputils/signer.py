from __future__ import annotations

import base64
import json
import typing

from datetime import datetime, timedelta
from functools import wraps
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request
from Crypto.PublicKey import RSA, ECC
from Crypto.Signature import PKCS1_v1_5, DSS

from .enums import AlgorithmType, KeyType
from .errors import SignatureFailureError
from .misc import HASHES, Digest, HttpDate, Signature

try:
	from aiohttp.web import BaseRequest as AiohttpRequest

except ImportError:
	AiohttpRequest = None

if typing.TYPE_CHECKING:
	from collections.abc import Callable, Sequence
	from typing import Any


def _check_private(func: Callable) -> Callable:
	"Checks if the key is a private key before running a method"

	@wraps(func)  # noqa: ANN201
	def wrapper(key: Signer, *args: Any, **kwargs: Any) -> Any:
		if not key.is_private:
			raise TypeError(f"Cannot use method '{func.__name__}' on Signer with public key")

		return func(key, *args, **kwargs)
	return wrapper


def _check_key_type(*types: KeyType | str) -> Callable:
	"Checks if the key is the correct type before running the method"

	types = tuple(KeyType.parse(type) for type in types)

	def outer(func: Callable):
		@wraps(func)  # noqa: ANN201
		def wrapper(signer: Signer, *args: Any, **kwargs: Any) -> Callable:
			if signer.type not in types:
				method = func.__name__
				alg = signer.type.value

				raise TypeError(f"Cannot use method '{method}' on Signer with {alg} key")

			return func(signer, *args, **kwargs)
		return wrapper
	return outer


class Signer:
	"Used to sign or verify HTTP headers"

	__test_mode: bool = False


	def __init__(self, key: str | Path | ECC.EccKey | RSA.RsaKey, keyid: str) -> None:
		"""
			Create a new signer object. The key can be an ``RsaKey`` object, ``str``, or ``Path`` to
			an exported key

			:param key: RSA or ECC key to use for signing or verifying
			:param keyid: Url to a web resource which hosts the public key
		"""

		self.key: ECC.EccKey | RSA.RsaKey = key # type: ignore
		"Key to use for signing or verifying"

		self.keyid: str = keyid
		"Url to a web resource which hosts the public key"


	def __repr__(self) -> str:
		if self.type == KeyType.RSA:
			return f"{self.__class__.__name__}(type='RSA', bits={self.bits}, keyid='{self.keyid}')"

		return f"{self.__class__.__name__}(type='ECC', keyid='{self.keyid}')"


	def __setattr__(self, key: str, value: Any) -> None:
		if key == "key":
			if isinstance(value, Path):
				with value.open("r") as fd:
					value = fd.read()

			if isinstance(value, str):
				if not value.startswith("-"):
					with Path(value).expanduser().resolve().open("r", encoding = "utf-8") as fd:
						value = fd.read()

				try:
					value = RSA.import_key(value)

				except ValueError:
					value = ECC.import_key(value)

					if value.curve != "Ed25519":
						msg = "Invalid ECC key. Only the Ed25519 curve is supported."
						raise TypeError(msg) from None

			elif not isinstance(value, (ECC.EccKey, RSA.RsaKey)):
				msg = "Key must be an RsaKey, EccKey, Path, or a string representation of a key"
				raise TypeError(msg)

		object.__setattr__(self, key, value)


	@staticmethod
	def create_sigstring(headers: dict[str, str], used_headers: Sequence[str]) -> bytes:
		"""
			Create a signing string from HTTP headers

			:param headers: Key/value pair of HTTP headers
			:param used_headers: List of headers to be used in the signing string
		"""
		string = "\n".join(f"{key}: {headers[key]}" for key in used_headers)
		return string.encode("ascii")


	# the current spec just uses sha256 for now, but keeping this function for future use
	@staticmethod
	def hash_func(algorithm: AlgorithmType) -> Callable:  # pylint: disable=unused-argument
		"""
			Get the hash function for the specified algorithm

			.. note:: The only hash algorithm used at the moment is SHA256

			:param algorithm: Type of algorithm used for the signature
		"""
		return HASHES["sha256"].new


	@property
	def sign_func(self) -> Callable:
		"Get the function necessary for signing"

		if self.type == KeyType.ECC:
			return DSS.new

		if self.type == KeyType.RSA:
			return PKCS1_v1_5.new

		raise NotImplementedError(self.type)


	def _generate_signature(self,
							headers: dict[str, str],
							used_headers: Sequence[str],
							algorithm: AlgorithmType) -> str:

		sig_string = Signer.create_sigstring(headers, used_headers)
		sighash = Signer.hash_func(algorithm)(data = sig_string)
		sigdata = self.sign_func(self.key).sign(sighash)

		return base64.b64encode(sigdata).decode("utf-8")


	def _validate_signature(self, headers: dict[str, str], signature: Signature) -> bool:
		hash_func = Signer.hash_func(signature.algorithm_type)

		return self.sign_func(self.key).verify(
			hash_func(data = Signer.create_sigstring(headers, signature.headers)),
			base64.b64decode(signature.signature)
		)


	@classmethod
	def new(cls: type[Signer],
			keyid: str,
			keytype: KeyType = KeyType.RSA,
			size: int = 4096) -> Signer:
		"""
			Create a new signer with a generated ``RsaKey`` of the specified size

			:param keyid: Url to a web resource which hosts the public key
			:param keytype: Type of private key to generate
			:param size: Size of RSA key in bits to generate. This is ignore for ECC keys.
		"""
		keytype = KeyType.parse(keytype)

		if keytype == KeyType.RSA:
			return cls(RSA.generate(size), keyid)

		if keytype == KeyType.ECC:
			return cls(ECC.generate(curve="Ed25519"), keyid)

		raise TypeError(f"Invalid key type: {keytype}")


	@classmethod
	def new_from_actor(cls: type[Signer], actor: dict[str, Any]) -> Signer:
		"""
			Create a signer object from an ActivityPub actor dict

			:param dict actor: ActivityPub Actor object
		"""

		return cls(actor["publicKey"]["publicKeyPem"], actor["publicKey"]["id"])


	@property
	@_check_key_type(KeyType.RSA)
	def bits(self) -> int:
		"Size of the RSA key in bits"
		return self.key.size_in_bits() # type: ignore


	@property
	def is_private(self) -> bool:
		"Return ``True`` if the key is private"
		return self.key.has_private()


	@property
	def type(self) -> KeyType:
		"Algorithm used to generate the key"
		if isinstance(self.key, ECC.EccKey):
			return KeyType.ECC

		if isinstance(self.key, RSA.RsaKey):
			return KeyType.RSA

		raise TypeError(f"Invalid key type: {self.key.__class__.__name__}")


	@property
	@_check_private
	def pubkey(self) -> str:
		"Export the public key to a str"
		key_data = self.key.public_key().export_key(format="PEM")
		return key_data.decode("utf-8") if isinstance(key_data, bytes) else key_data


	def export(self, path: Path | str | None = None) -> str:
		"""
			Export the key to a str

			:param path: Path to dump the key in text form to if specified
		"""
		key_data = self.key.export_key(format = "PEM")
		key = key_data.decode("utf-8") if isinstance(key_data, bytes) else key_data

		if path:
			path = Path(path)

			with path.open("w", encoding = "utf-8") as fd:
				fd.write(key)

		return key


	@_check_private
	def sign_headers(self,
					method: str,
					url: str,
					data: dict[str, Any] | None = None,
					headers: dict[str, Any] | None = None,
					sign_all: bool = False,
					algorithm: AlgorithmType = AlgorithmType.HS2019) -> dict[str, Any]:
		"""
			Generate a signature and return the headers with a "Signature" key

			Note: HS2019 is the only supported algorithm, so only use others when you absolutely
			have to

			:param method: HTTP method of the request
			:param url: URL of the request
			:param data: ActivityPub message for a POST request
			:param headers: Request headers
			:param sign_all: If ``True``, sign all headers instead of just the required ones
			:param algorithm: Type of algorithm to use for hashing the headers. HS2019 is the only
				non-deprecated algorithm.
		"""

		if headers is None:
			headers = {}

		else:
			headers = {key.lower(): value for key, value in headers.items()}

		date = headers.get("date", HttpDate.new_utc())

		if isinstance(date, str):
			date = HttpDate.parse(date)

		elif isinstance(date, datetime):
			if date.__class__ is datetime:
				date = HttpDate.new_from_datetime(date)

			headers["date"] = date.to_string()

		URL = urlparse(url)
		used_headers = ["(request-target)", "host", "date"]
		headers.update({
			"(request-target)": f"{method.lower()} {URL.path}",
			"host": URL.netloc
		})

		if algorithm == AlgorithmType.HS2019:
			signature_alg = "hs2019"
			used_headers.extend(["(created)", "(expires)"])
			headers.update({
				"(created)": str(date.timestamp()),
				"(expires)": str((date + timedelta(hours=6)).timestamp())
			})

		else:
			signature_alg = f"{self.type.value}-sha256"

		if data:
			used_headers.extend(["digest", "content-length"])
			body = json.dumps(data)
			headers.update({
				"digest": Digest.new(body).compile(),
				"content-length": str(len(body.encode("utf-8")))
			})

		if sign_all:
			for key in headers:
				if key not in used_headers:
					used_headers.append(key)

		signature = Signature(
			keyid = self.keyid,
			algorithm = signature_alg,
			headers = used_headers,
			signature = self._generate_signature(headers, used_headers, algorithm)
		)

		if algorithm == AlgorithmType.HS2019:
			signature.created = int(headers["(created)"])
			signature.expires = int(headers["(expires)"])

		headers["signature"] = signature.compile()

		for key in tuple(headers.keys()):
			if key.startswith("(") or key == "host":
				del headers[key]

		return headers


	@_check_private
	def sign_request(self, request: Request, algorithm: AlgorithmType = AlgorithmType.HS2019) -> Any:
		"""
			Convenience function to sign a request. Support for more Request classes planned.

			:param request: Request object to sign
			:param algorithm: Type of algorithm to use for signing and hashing the headers. HS2019
				is the only non-deprecated algorithm.

			:raises TypeError: If the Request class is not supported
		"""

		# sign built-in request class
		if isinstance(request, Request):
			request_headers = dict(request.header_items())
			headers = self.sign_headers(
				request.get_method().upper(),
				request.full_url, request.data,
				request_headers,
				algorithm = algorithm
			)

			request.headers = {key.title(): value for key, value in headers.items()}

		else:
			raise TypeError(f"Request from module not supported: {type(request).__module__}")

		return request


	def validate_signature(self,
						method: str,
						path: str,
						headers: dict[str, Any],
						body: "bytes" | str | None = None) -> bool:
		"""
			Check to make sure the Signature and Digest headers match

			:param method: Request method
			:param path: Request path
			:param headers: Request headers
			:param body: Request body if it exists

			:raises aputils.SignatureFailureError: When any step of the validation process fails
		"""

		headers = {key.lower(): value for key, value in headers.items()}
		headers["(request-target)"] = " ".join([method.lower(), path])
		digest = Digest.new_from_digest(headers.get("digest"))

		try:
			sig = Signature.new_from_headers(headers)

		except KeyError:
			raise SignatureFailureError("Missing signature") from None

		if digest:
			if not body:
				raise SignatureFailureError("Missing body for digest verification")

			if not digest.validate(body):
				raise SignatureFailureError("Body digest does not match")

		if sig.algorithm_type == AlgorithmType.HS2019:
			if "(created)" not in sig.headers:
				raise SignatureFailureError("'(created)' header not used")

			if not sig.created or not sig.expires:
				raise SignatureFailureError("Missing 'created' and/or 'expires' option")

			if not self.__test_mode:
				current_timestamp = HttpDate.new_utc().timestamp()

				if sig.created > current_timestamp:
					raise SignatureFailureError("Creation date after current date")

				if current_timestamp > sig.expires:
					raise SignatureFailureError("Expiration date before current date")

			headers["(created)"] = sig.created
			headers["(expires)"] = sig.expires

		# pycryptodome 3.17 raises a ValueError instead of returning False
		try:
			valid = self._validate_signature(headers, sig)

		except ValueError:
			valid = False

		if not valid:
			raise SignatureFailureError("Signature does not match")

		return valid


	if AiohttpRequest is not None:
		async def validate_aiohttp_request(self, request: AiohttpRequest) -> bool:
			"""
				Validate the signature header of an AIOHTTP server request object

				:param request: AioHttp server request to validate
			"""
			return self.validate_signature(
				request.method,
				request.path,
				request.headers,
				await request.read()
			)
