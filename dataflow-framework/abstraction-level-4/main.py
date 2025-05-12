from typing import Iterator, Optional
from dotenv import load_dotenv
from pipeline import load_pipeline_from_config
from core import apply_processors

DEFAULT_CONFIG_PATH = "pipeline.yaml"

def read_lines(file_path: str) -> Iterator[str]:
    with open(file_path, 'r') as file: 
        for line in file:
            yield line


def write_lines(lines: Iterator[str], output_path: Optional[str]) -> None:
    def flatten_line(line):
        if isinstance(line, str):
            return [line]
        elif isinstance(line, Iterator):
            return list(line)
        else:
            return [str(line)]

    if output_path:
        with open(output_path, 'w') as file:
            for line in lines:
                if line is None:
                    continue
                for l in flatten_line(line):
                    file.write(l + '\n')
    else:
        for line in lines:
            if line is None:
                continue
            for l in flatten_line(line):
                print(l)
            
def complete_process(
    input_file: str,
    output_file: Optional[str],
    config_path: Optional[str] = DEFAULT_CONFIG_PATH,
) -> None:
    processors = load_pipeline_from_config(config_path)
    lines = read_lines(input_file)
    processed_lines = (apply_processors(line, processors) for line in lines)
    write_lines(processed_lines, output_file)
    
    
# if __name__ == "__main__":
#     import sys
#     input_file = sys.argv[1]
#     output_file = sys.argv[2] if len(sys.argv) > 2 else None
#     config_file = sys.argv[3] if len(sys.argv) > 3 else DEFAULT_CONFIG_PATH
    
#     complete_process(input_file, output_file, config_file)