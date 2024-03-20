from logging import basicConfig, getLogger, INFO as LOGGING_INFO

from .archive import compress, extract
from .async_executor import AsyncExecutor
from .config import load_config
from .pbtxt import (
    PbtxtDocument,
    PbtxtField,
    PbtxtList,
    PbtxtObject,
    PbtxtParser,
    PbtxtValue,
    PbtxtValueType,
)

basicConfig(
    level=LOGGING_INFO,
    format="[%(asctime)s %(process)d %(filename)s:%(lineno)d] %(message)s",
    datefmt="%H:%M:%S",
)
client_logger = getLogger("client_logger")

__all__ = [
    "AsyncExecutor",
    "client_logger",
    "compress",
    "extract",
    "load_config",
    "PbtxtDocument",
    "PbtxtField",
    "PbtxtList",
    "PbtxtObject",
    "PbtxtParser",
    "PbtxtValue",
    "PbtxtValueType",
]
