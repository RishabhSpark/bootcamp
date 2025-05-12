from abc import ABC, abstractmethod

class LineTagger(ABC):
    @abstractmethod
    def __call__(self, line: str):
        pass

class TagError(LineTagger):
    def __call__(self, line: str):
        if "error" in line.lower():
            yield ("errors", line)
        else:
            yield ("general", line)

class TagWarn(LineTagger):
    def __call__(self, line: str):
        if "warn" in line.lower():
            yield ("warnings", line)
        else:
            yield ("general", line)
