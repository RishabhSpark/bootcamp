from typing import Callable, Iterator, Union, Tuple

LineProcessor = Callable[[str], str]
StreamProcessor = Callable[[Iterator[str]], Iterator[str]]
ProcessorFn = Union[LineProcessor, StreamProcessor]
TaggedLine = Tuple[str, str]