from .core import to_snakecase, to_uppercase
from .custom_types import ProcessorFn
from typing import List

def pipeline(mode: str) -> List[ProcessorFn]:
    if mode == "uppercase":
        return [to_uppercase]
    elif mode == "snakecase":
        return [to_snakecase]
    else:
        raise ValueError(f"Unknown mode: {mode}")