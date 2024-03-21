__software__ = "Gemi"
__version__ = "0.1.1"

import mimetypes
mimetypes.add_type("text/gemini", ".gmi", strict = True)

from .client import AsyncClient
from .enums import AppType, FileSizeUnit, OutputFormat, StatusCode, Enum, IntEnum, StrEnum
from .error import BodyTooLargeError, GeminiError, ParsingError
from .message import Message, Request, Response
from .server import AsyncServer, Router, BaseRoute, Route, FileRoute, route
from .transport import AsyncTransport

from .document import (
	Document,
	Element,
	Header,
	Link,
	ListItem,
	Preformatted,
	Quote,
	Text
)

from .misc import (
	BaseApp,
	FileSize,
	SslContext,
	Url,
	convert_to_bytes,
	convert_to_string,
	resolve_path
)
