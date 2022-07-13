import logging
from typing import (
    IO,
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
)

from botocore.awsrequest import AWSRequest
from s3transfer.compat import SOCKET_ERROR as SOCKET_ERROR
from s3transfer.compat import fallocate as fallocate
from s3transfer.compat import rename_file as rename_file
from s3transfer.futures import TaskTag, TransferFuture

_R = TypeVar("_R")

MAX_PARTS: int
MAX_SINGLE_UPLOAD_SIZE: int
MIN_UPLOAD_CHUNKSIZE: int
logger: logging.Logger
S3_RETRYABLE_DOWNLOAD_ERRORS: Tuple[Type[BaseException], ...]

def random_file_extension(num_digits: int = ...) -> str: ...
def signal_not_transferring(request: AWSRequest, operation_name: str, **kwargs: Any) -> None: ...
def signal_transferring(request: AWSRequest, operation_name: str, **kwargs: Any) -> None: ...
def calculate_num_parts(size: int, part_size: int) -> int: ...
def calculate_range_parameter(
    part_size: int, part_index: int, num_parts: int, total_size: Optional[int] = ...
) -> str: ...
def get_callbacks(
    transfer_future: TransferFuture, callback_type: str
) -> List[Callable[..., Any]]: ...
def invoke_progress_callbacks(
    callbacks: Iterable[Callable[..., Any]], bytes_transferred: int
) -> None: ...
def get_filtered_dict(
    original_dict: Dict[str, Any], whitelisted_keys: Sequence[str]
) -> Dict[str, Any]: ...

class CallArgs:
    def __init__(self, **kwargs: Any) -> None: ...

class FunctionContainer:
    def __init__(self, func: Callable[..., Any], *args: Any, **kwargs: Any) -> None: ...
    def __call__(self) -> Any: ...

class CountCallbackInvoker:
    def __init__(self, callback: Callable[..., Any]) -> None: ...
    @property
    def current_count(self) -> int: ...
    def increment(self) -> None: ...
    def decrement(self) -> None: ...
    def finalize(self) -> None: ...

class OSUtils:
    def get_file_size(self, filename: str) -> int: ...
    def open_file_chunk_reader(
        self, filename: str, start_byte: int, size: int, callbacks: Iterable[Callable[..., Any]]
    ) -> ReadFileChunk: ...
    def open_file_chunk_reader_from_fileobj(
        self,
        fileobj: IO[Any],
        chunk_size: int,
        full_file_size: int,
        callbacks: Iterable[Callable[..., Any]],
        close_callbacks: Optional[Iterable[Callable[..., Any]]] = ...,
    ) -> ReadFileChunk: ...
    def open(self, filename: str, mode: str) -> IO[Any]: ...
    def remove_file(self, filename: str) -> None: ...
    def rename_file(self, current_filename: str, new_filename: str) -> None: ...
    def is_special_file(cls, filename: str) -> bool: ...
    def get_temp_filename(self, filename: str) -> str: ...
    def allocate(self, filename: str, size: int) -> None: ...

class DeferredOpenFile:
    def __init__(
        self,
        filename: str,
        start_byte: int = ...,
        mode: str = ...,
        open_function: Callable[..., Any] = ...,
    ) -> None: ...
    @property
    def name(self) -> str: ...
    def read(self, amount: Optional[int] = ...) -> bytes: ...
    def write(self, data: str) -> None: ...
    def seek(self, where: int, whence: int = ...) -> None: ...
    def tell(self) -> int: ...
    def close(self) -> None: ...
    def __enter__(self: _R) -> _R: ...
    def __exit__(self, *args: Any, **kwargs: Any) -> None: ...

class ReadFileChunk:
    def __init__(
        self,
        fileobj: IO[Any],
        chunk_size: int,
        full_file_size: int,
        callbacks: Optional[Iterable[Callable[..., Any]]] = ...,
        enable_callbacks: bool = ...,
        close_callbacks: Optional[Iterable[Callable[..., Any]]] = ...,
    ) -> None: ...
    @classmethod
    def from_filename(
        cls: Type[_R],
        filename: str,
        start_byte: int,
        chunk_size: int,
        callbacks: Optional[Iterable[Callable[..., Any]]] = ...,
        enable_callbacks: bool = ...,
    ) -> _R: ...
    def read(self, amount: Optional[int] = ...) -> bytes: ...
    def signal_transferring(self) -> None: ...
    def signal_not_transferring(self) -> None: ...
    def enable_callback(self) -> None: ...
    def disable_callback(self) -> None: ...
    def seek(self, where: int, whence: int = ...) -> None: ...
    def close(self) -> None: ...
    def tell(self) -> int: ...
    def __len__(self) -> int: ...
    def __enter__(self: _R) -> _R: ...
    def __exit__(self, *args: Any, **kwargs: Any) -> None: ...
    def __iter__(self) -> Iterator[bytes]: ...

class StreamReaderProgress:
    def __init__(
        self, stream: IO[Any], callbacks: Optional[Iterable[Callable[..., Any]]] = ...
    ) -> None: ...
    def read(self, *args: Any, **kwargs: Any) -> bytes: ...

class NoResourcesAvailable(Exception): ...

class TaskSemaphore:
    def __init__(self, count: int) -> None: ...
    def acquire(self, tag: TaskTag, blocking: bool = ...) -> int: ...
    def release(self, tag: TaskTag, acquire_token: int) -> None: ...

class SlidingWindowSemaphore(TaskSemaphore):
    def __init__(self, count) -> None: ...
    def current_count(self) -> int: ...
    def acquire(self, tag: TaskTag, blocking: bool = ...) -> int: ...
    def release(self, tag: TaskTag, acquire_token: int) -> None: ...

class ChunksizeAdjuster:
    max_size: int
    min_size: int
    max_parts: int
    def __init__(self, max_size: int = ..., min_size: int = ..., max_parts: int = ...) -> None: ...
    def adjust_chunksize(self, current_chunksize: int, file_size: Optional[int] = ...) -> int: ...