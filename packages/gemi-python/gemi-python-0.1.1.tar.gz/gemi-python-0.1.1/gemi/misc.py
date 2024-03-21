from __future__ import annotations

import json
import ssl
import typing

from pathlib import Path
from urllib.parse import urlparse

from .enums import AppType, FileSizeUnit

try:
	from OpenSSL import crypto

except ImportError:
	crypto = None # type: ignore

if typing.TYPE_CHECKING:
	from collections.abc import Sequence
	from typing import Any, Self
	from .client import AsyncClient
	from .server import AsyncServer


def convert_to_bytes(value: Any, encoding: str = "utf-8") -> bytes:
	"""
		Convert an object to :class:`bytes`

		:param value: Object to be converted
		:param encoding: Character encoding to use if the object is a string or gets converted to
			one in the process
		:raises TypeError: If the object cannot be converted
	"""

	if isinstance(value, bytes):
		return value

	try:
		return convert_to_string(value).encode(encoding)

	except TypeError:
		raise TypeError(f"Cannot convert '{type(value).__name__}' into bytes") from None


def convert_to_string(value: Any, encoding: str = 'utf-8') -> str:
	"""
		Convert an object to :class:`str`

		:param value: Object to be converted
		:param encoding: Character encoding to use if the object is a :class:`bytes` object
	"""

	if isinstance(value, bytes):
		return value.decode(encoding)

	if isinstance(value, bool):
		return str(value)

	if isinstance(value, str):
		return value

	if isinstance(value, (dict, list, tuple, set)):
		return json.dumps(value)

	if isinstance(value, (int, float)):
		return str(value)

	if value is None:
		return ''

	raise TypeError(f'Cannot convert "{type(value).__name__}" into a string') from None


def resolve_path(path: Path | str) -> Path:
	if isinstance(path, str):
		path = Path(path)

	return path.expanduser().resolve()


class BaseApp:
	"Base properties for the client and server classes"

	apptype: AppType
	"Whether the application is a client or server"


	def __init__(self,
				name: str,
				cert: Path | str | None = None,
				key: Path | str | None = None,
				timeout: int = 30):

		if type(self) is BaseApp:
			raise NotImplementedError("This class should not be used by itself")

		self.name: str = name
		"Internal name of the application"

		self.timeout: int = timeout
		"Length in seconds to wait for a network action"

		self.ssl_context: SslContext = SslContext(self, cert, key)
		"Context object used for SSL actions"


class FileSize(int):
	"Converts a human-readable file size to bytes"


	def __init__(self, size: int | float, unit: FileSizeUnit | str = FileSizeUnit.B):
		"""
			Create a new FileSize object

			:param size: Size of the file
			:param unit: Unit notation
		"""

		self.size: int | float = size
		self.unit: FileSizeUnit = FileSizeUnit.parse(unit)


	def __new__(cls, size: int | float, unit: FileSizeUnit | str = FileSizeUnit.B):
		return int.__new__(cls, FileSizeUnit.parse(unit).multiply(size))


	def __repr__(self):
		value = int(self)
		return f"FileSize({value:,} bytes)"


	def __str__(self):
		return str(int(self))


	@classmethod
	def parse(cls: type[Self], text: str) -> Self:
		"""
			Parse a file size string

			:param text: String representation of a file size
			:raises AttributeError: If the text cannot be parsed
		"""

		size, unit = text.strip().split(" ", 1)
		return cls(float(size), FileSizeUnit.parse(unit))


	def to_optimal_string(self) -> str:
		"""
			Attempts to display the size as the highest whole unit
		"""

		index = 0
		size: int | float = int(self)

		while True:
			if size < 1024 or index == 8:
				unit = FileSizeUnit.from_index(index)
				return f'{size:.2f} {unit}'

			try:
				index += 1
				size = self / FileSizeUnit.from_index(index).multiplier

			except IndexError:
				raise ValueError('File size is too large to convert to a string') from None


	def to_string(self, unit: FileSizeUnit, decimals: int = 2) -> str:
		"""
			Convert to the specified file size unit

			:param unit: Unit to convert to
			:param decimals: Number of decimal points to round to
		"""

		unit = FileSizeUnit.parse(unit)

		if unit == FileSizeUnit.BYTE:
			return f'{self} B'

		size = round(self / unit.multiplier, decimals)
		return f'{size} {unit}'


class SslContext(ssl.SSLContext):
	client: AsyncClient
	"Client object the context is associated with"

	server: AsyncServer
	"Server object the context is associated with"

	cert: Path
	"Path to the certificate file in PEM format"

	key: Path
	"Path to the key file in PEM format"


	def __init__(self,
				app: BaseApp,
				cert: Path | str | None = None,
				key: Path | str | None = None):

		ssl.SSLContext.__init__(self)

		self.check_hostname: bool = False
		self.verify_mode = ssl.CERT_NONE

		self.cert: Path | None = resolve_path(cert) if cert else None # type: ignore
		self.key: Path | None = resolve_path(key) if key else None # type: ignore

		if app.apptype == AppType.CLIENT:
			self.client = app # type: ignore

		else:
			if not (cert or key):
				raise ValueError("Must set certificate and private key for server")

			self.server = app # type: ignore


	def __new__(cls: type[Self], app: BaseApp, *_) -> Self:
		if app.apptype == AppType.CLIENT:
			protocol = ssl.PROTOCOL_TLS_CLIENT

		else:
			protocol = ssl.PROTOCOL_TLS_SERVER

		return ssl.SSLContext.__new__(cls, protocol)


	def generate_cert(self, hostname: str, overwrite: bool = False) -> None:
		if crypto is None:
			raise RuntimeError("pyOpenSSL module is not installed")

		if not overwrite and (self.cert.exists() or self.key.exists()):
			raise FileExistsError("Not willing to overwrite the key and certificate")

		key = crypto.PKey()
		key.generate_key(crypto.TYPE_RSA, 4096)

		cert = crypto.X509()
		subject = cert.get_subject()
		subject.C = "US"
		subject.ST = "New Jersey"
		subject.L = "Camden"
		subject.O = "Barkshark" # noqa: E741
		subject.OU = "Barkshark"
		subject.CN = hostname
		cert.set_serial_number(1000)
		cert.gmtime_adj_notBefore(0)
		cert.gmtime_adj_notAfter(10*365*24*60*60)
		cert.set_issuer(cert.get_subject())
		cert.set_pubkey(key)
		cert.sign(key, "sha1")

		with self.cert.open("wb") as fd:
			fd.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))

		with self.key.open("wb") as fd:
			fd.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))


	def load_cert(self) -> None:
		self.load_cert_chain(certfile = self.cert, keyfile = self.key)


class Url(str):
	"Represents a Gemini or Tital URL with properties for each part"


	def __init__(self,
				domain: str,
				path: str,
				proto: str = "gemini",
				port: int = 0,
				query: Sequence[str] | None = None,
				anchor: str | None = None):
		"""
			Create a new Url object

			:param domain: Domain of the url
			:param path: Path of the url
			:param proto: Protocol of the url
			:param port: Port of the url
			:param query: Mapping of key/value pairs for the query part of the url
			:param anchor: Extra text at the end of the url
		"""

		assert port >= 0, "Port must be at least 0"

		self.parts: tuple[str, str, str, int, tuple[str, ...], str | None] = (
			domain, path, proto, port, tuple(query or []), anchor
		)


	def __new__(cls,
				domain: str,
				path: str,
				proto: str = "gemini",
				port: int = 0,
				query: Sequence[str] | None = None,
				anchor: str | None = None) -> Self:

		if proto.lower() not in {"gemini", "titan"}:
			raise ValueError("Protocol must be 'gemini' or 'titan'")

		url = f"{proto}://{domain}"

		if port:
			url += f":{port}"

		url += "/" + path if not path.startswith("/") else path

		if query:
			url += f"?{'&'.join(query)}"

		if anchor:
			url += f"#{anchor}"

		return str.__new__(cls, url)


	@classmethod
	def parse(cls: type[Self], url: str) -> Self:
		"""
			Parse a URL string

			:param url: URL as a string
		"""

		if isinstance(url, cls):
			return url

		if not url.startswith(("gemini://", "titan://")):
			url = f"gemini://{url}"

		data = urlparse(url)

		if data.scheme.lower() not in {"gemini", "titan"}:
			raise ValueError("Protocol must be 'gemini' or 'titan'")

		if data.hostname is None:
			raise ValueError("Hostname cannot be empty")

		return cls(
			data.hostname,
			data.path or "/",
			data.scheme.lower(),
			data.port or 0,
			data.query,
			data.fragment
		)


	@property
	def domain(self) -> str:
		"Domain of the url"

		return self.parts[0]


	@property
	def path(self) -> str:
		"Path of the url"

		return self.parts[1]


	@property
	def proto(self) -> str:
		"Protocol of the url"

		return self.parts[2]


	@property
	def port(self) -> int:
		"""
			Port of the url. If no port is listed in the url, the default for the protocol will be
			returned
		"""

		return self.parts[3] or 1965


	@property
	def query(self) -> tuple[str, ...]:
		"Mapping of key/value pairs for the query part of the url"

		return self.parts[4]


	@property
	def anchor(self) -> str | None:
		"Extra text at the end of the url"

		return self.parts[5]


	@property
	def hostname(self) -> str:
		"""
			Get the hostname of the url. If the default port for the protocol is used, just return
			the domain.
		"""

		if self.parts[3] < 1:
			return self.domain

		return f"{self.domain}:{self.port}"
