from typing import Iterator, Optional
from dotenv import load_dotenv
import os
from .pipeline import pipeline
from .core import apply_processors

load_dotenv()
DEFAULT_MODE = os.getenv("MODE", "uppercase")

def read_lines(file_path: str) -> Iterator[str]:
    with open(file_path, 'r') as file: 
        for line in file:
            yield line


def write_lines(lines: Iterator[str], output_path: Optional[str]) -> None:
    if output_path:
        with open(output_path, 'w') as file:
            for line in lines:
                file.write(line)
    else:
        for line in lines:
            print(line)
            
def complete_process(
    input_file: str,
    output_file: Optional[str],
    mode: Optional[str],
) -> None:
    mode = mode or DEFAULT_MODE
    processors = pipeline(mode)
    processed_lines = (apply_processors(line, processors) for line in read_lines(input_file))
    write_lines(processed_lines, output_file)
