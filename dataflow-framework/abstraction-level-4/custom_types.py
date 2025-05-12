from typing import Callable, Iterator, Union

LineProcessor = Callable[[str], str]
StreamProcessor = Callable[[Iterator[str]], Iterator[str]]
ProcessorFn = Union[LineProcessor, StreamProcessor]
