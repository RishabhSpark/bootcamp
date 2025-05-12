from typing import Iterator, Optional
from pipeline import load_dag_pipeline

DEFAULT_CONFIG_PATH = "dag_pipeline.yaml"

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
    dag = load_dag_pipeline(config_path)

    processed_lines = []

    # Process each line in the input file
    with open(input_file, 'r') as f:
        for line in f:
            # Process each line and capture the output
            dag.process(line.strip())

    processed_lines = dag.process(line.strip()) or []
    write_lines(processed_lines, output_file)
