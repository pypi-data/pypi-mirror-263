from __future__ import annotations

import asyncio
import typing

from contextlib import contextmanager

from .misc import convert_to_bytes

if typing.TYPE_CHECKING:
	from typing import Any


class AsyncTransport:
	"Transport class for ``StreamReader`` and ``StreamWriter`` objects"


	def __init__(self,
				reader: asyncio.StreamReader,
				writer: asyncio.StreamWriter,
				timeout: int = 60,
				encoding: str = 'utf-8',):
		"""
			Create a new async transport

			:param reader: Reader object
			:param writer: Writer object
			:param timeout: Time to wait for read methods before giving up
			:param encoding: Text encoding to use when decoding raw data into text
		"""

		self.reader: asyncio.StreamReader = reader
		"Reader object"

		self.writer: asyncio.StreamWriter = writer
		"Writer object"

		self.encoding: str = encoding
		"Text encoding to use when converting text into bytes"

		self.timeout: int = timeout
		"Time to wait for read methods before giving up"


	@property
	def eof(self) -> bool:
		"Checks if the reader has reached the end of the stream"

		return self.reader.at_eof()


	@property
	def local_address(self) -> str:
		"Get the address of the local socket"

		return self.writer.get_extra_info('sockname')[0]


	@property
	def local_port(self) -> str:
		"Get the port of the local socket"

		return self.writer.get_extra_info('sockname')[1]


	@property
	def remote_address(self) -> str:
		"Get the address of the remote socket"

		return self.writer.get_extra_info('peername')[0]


	@property
	def remote_port(self) -> str:
		"Get the port of the remote socket"

		return self.writer.get_extra_info('peername')[1]


	@property
	def client_port(self) -> int:
		"Get the port of the lcient"

		return self.writer.get_extra_info('peername')[1]


	async def close(self) -> None:
		"Close the writer stream"

		if self.writer.can_write_eof():
			self.writer.write_eof()

		self.writer.close()
		await self.writer.wait_closed()


	async def read(self, length: int = -1) -> bytes:
		"""
			Read a chunk of data

			:param length: Amount of data in bytes to read
		"""

		return await asyncio.wait_for(self.reader.read(length), self.timeout)


	async def readline(self, limit: int = 65536) -> bytes:
		"Read until a line ending ('\\\\r' or '\\\\n') is encountered"

		with self._set_limit(limit):
			return await asyncio.wait_for(self.reader.readline(), self.timeout)


	async def readuntil(self, separator: bytes | str, limit = 65536) -> bytes:
		"""
			Read upto the separator

			:param separator: Text or bytes to stop at
		"""

		if isinstance(separator, str):
			separator = separator.encode(self.encoding)

		with self._set_limit(limit):
			return await asyncio.wait_for(self.reader.readuntil(separator), self.timeout)


	async def write(self, data: Any) -> None:
		"""
			Send data

			:param data: Data to be sent
		"""

		data = convert_to_bytes(data, self.encoding)
		self.writer.write(data)
		await self.writer.drain()


	@contextmanager
	def _set_limit(self, limit: int = 65536):
		orig_limit = self.reader._limit
		self.reader._limit = limit

		try:
			yield

		finally:
			self.reader._limit = orig_limit
