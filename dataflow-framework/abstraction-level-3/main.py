from typing import Iterator, Optional
from pipeline import load_pipeline_from_config
from core import apply_processors

DEFAULT_CONFIG_PATH = "pipeline.yaml"

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
    config_path: Optional[str],
) -> None:
    config_path = config_path or DEFAULT_CONFIG_PATH
    processors = load_pipeline_from_config(config_path)
    lines = read_lines(input_file)
    processed_lines = (apply_processors(line, processors) for line in lines)
    write_lines(processed_lines, output_file)