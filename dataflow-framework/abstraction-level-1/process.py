import os
import typer
from dotenv import load_dotenv
from typing import Optional, Iterator

load_dotenv()

DEFAULT_MODE = os.getenv("MODE", "uppercase")

app = typer.Typer()

def read_lines(file_path: str) -> Iterator[str]:
    with open(file_path, 'r') as file: 
        for line in file:
            yield line
            
            
def transform_line(line: str, mode: str) -> str:
    if mode == "uppercase":
        return line.upper()
    elif mode == 'snakecase':
        return line.replace(" ", "_").lower()
    else:
        raise ValueError(f"Unknown mode: {mode}")

def write_lines(lines: Iterator[str], output_path: Optional[str]) -> None:
    if output_path:
        with open(output_path, 'w') as file:
            for line in lines:
                file.write(line)
    else:
        for line in lines:
            print(line)
            
@app.command()
def process(
    input_file: str = typer.Option(..., "--input", "-i", help="Path to the input file"),
    output_file: str = typer.Option(None, "--output", "-o", help="Path to the output file"),
    mode: str = typer.Option(DEFAULT_MODE, "--mode", "-m", help="Processing mode (uppercase/snakecase)"),
):
    lines = read_lines(input_file)
    transformed_lines = (transform_line(line, mode) for line in lines)
    write_lines(transformed_lines, output_file)

if __name__ == "__main__":
    app()