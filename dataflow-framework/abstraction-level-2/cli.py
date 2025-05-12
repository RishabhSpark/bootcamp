import typer
from .main import complete_process
from dotenv import load_dotenv
import os

load_dotenv()
DEFAULT_MODE = os.getenv("MODE", "uppercase")

app = typer.Typer()

@app.command()
def process(
    input_file: str = typer.Option(..., "--input", "-i", help="Path to the input file"),
    output_file: str = typer.Option(None, "--output", "-o", help="Path to the output file"),
    mode: str = typer.Option(DEFAULT_MODE, "--mode", "-m", help="Processing mode (uppercase/snakecase)"),
):
    """
    Process the input file and write the output to a file or print it.
    """
    complete_process(input_file, output_file, mode)
    

if __name__ == "__main__":
    app()