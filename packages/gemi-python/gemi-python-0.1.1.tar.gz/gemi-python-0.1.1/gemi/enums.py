from __future__ import annotations

import enum
import typing

if typing.TYPE_CHECKING:
	from typing import Any, Self


class Enum(enum.Enum):
	"Base enum class for all other enums"


	@classmethod
	def from_index(cls: type[Self], index: int) -> Self:
		return list(cls)[index]


	@classmethod
	def parse(cls: type[Self], data: Any) -> Self:
		"""
			Get an enum item by name or value

			:param data: Name or value
			:raises AttributeError: If an item could not be found
		"""

		if isinstance(data, cls):
			return data

		try:
			return cls[data]

		except KeyError:
			pass

		try:
			return cls(data)

		except ValueError:
			pass

		if isinstance(data, str):
			for item in cls:
				if issubclass(cls, StrEnum) and data.lower() == item.value.lower():
					return item

				if data.lower() == item.name.lower():
					return item

		raise AttributeError(f'Invalid enum property for {cls.__name__}: {data}')


class IntEnum(enum.IntEnum, Enum):
	"Enum where items can be treated like an :class:`int`"


class StrEnum(str, Enum):
	"Enum where items can be treated like a :class:`str`"

	def __str__(self):
		return self.value


class AppType(Enum):
	SERVER = enum.auto()
	CLIENT = enum.auto()


class FileSizeUnit(StrEnum):
	"Unit identifier for various file sizes"


	BYTE = 'B'

	KIBIBYTE = 'KiB'
	MEBIBYTE = 'MiB'
	GIBIBYTE = 'GiB'
	TEBIBYTE = 'TiB'
	PEBIBYTE = 'PiB'
	EXBIBYTE = 'EiB'
	ZEBIBYTE = 'ZiB'
	YOBIBYTE = 'YiB'

	KILOBYTE = 'KB'
	MEGABYTE = 'MB'
	GIGABYTE = 'GB'
	TERABYTE = 'TB'
	PETABYTE = 'PB'
	EXABYTE = 'EB'
	ZETTABYTE = 'ZB'
	YOTTABYTE = 'YB'

	B = BYTE
	K = KIBIBYTE
	M = MEBIBYTE
	G = GIBIBYTE
	T = TEBIBYTE
	P = PEBIBYTE
	E = EXBIBYTE
	Z = ZEBIBYTE
	Y = YOBIBYTE


	@property
	def multiplier(self) -> int:
		"Get the multiplier for the unit"

		match str(self):
			case "B":
				return 1

			case "KiB":
				return 1024
			case "MiB":
				return 1024 ** 2
			case "GiB":
				return 1024 ** 3
			case "TiB":
				return 1024 ** 4
			case "PiB":
				return 1024 ** 5
			case "EiB":
				return 1024 ** 6
			case "ZiB":
				return 1024 ** 7
			case "YiB":
				return 1024 ** 8

			case "KB":
				return 1000
			case "MB":
				return 1000 ** 2
			case "GB":
				return 1000 ** 3
			case "TB":
				return 1000 ** 4
			case "PB":
				return 1000 ** 5
			case "EB":
				return 1000 ** 6
			case "ZB":
				return 1000 ** 7
			case "YB":
				return 1000 ** 8

		# *shrugs*
		return 69_420


	def multiply(self, size: int | float) -> int | float:
		"""
			Multiply a file size to get the size in bytes

			:param size: File size to be multiplied
		"""

		return self.multiplier * size


class OutputFormat(Enum):
	"Text format to use when dumping a document"

	GEMTEXT = enum.auto()
	HTML = enum.auto()
	MARKDOWN = enum.auto()


class StatusCode(IntEnum):
	"Name and value for each code that can be returned from a server"

	INPUT = 10
	SENSITIVE_INPUT = 11

	SUCCESS = 20

	TEMPORARY_REDIRECT = 30
	PERMANENT_REDIRECT = 31

	TEMPORARY_FAILURE = 40
	SERVER_UNAVAILABLE = 41
	CGI_ERROR = 42
	PROXY_ERROR = 43
	SLOW_DOWN = 44

	PERMANENT_FAILURE = 50
	NOT_FOUND = 51
	GONE = 52
	PROXY_REQUEST_REFUSED = 53
	BAD_REQUEST = 59

	CERT_REQUIRED = 60
	CERT_NOT_AUTHORIZED = 61
	CERT_NOT_VALID = 62


	@property
	def reason(self) -> str:
		"Get the human readable name of the status"

		return self.name.replace("_", " ").title()
