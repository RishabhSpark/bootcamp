import re
from abc import ABC, abstractmethod


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, line: str) -> str:
        pass

    def process(self, line: str):
        formatted = self.format(line)
        return [("output", formatted)]


class UppercaseFormatter(BaseFormatter):
    def format(self, line: str) -> str:
        return line.upper()

class SnakecaseFormatter(BaseFormatter):
    def format(self, line: str) -> str:
        words = re.findall(r'\w+', line.lower())
        snake = "_".join(words)
        return snake