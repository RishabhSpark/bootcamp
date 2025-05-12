import typer
from main import complete_process
from dotenv import load_dotenv
import os

load_dotenv()

app = typer.Typer()

@app.command()
def process(
    input_file: str = typer.Option(..., "--input", "-i", help="Path to the input file"),
    output_file: str = typer.Option(None, "--output", "-o", help="Path to the output file"),
    config_path: str = typer.Option("pipeline.yaml", "--config", "-c", help="Path to the pipeline config file"),
):
    """
    Process the input file and write the output to a file or print it.
    """
    config_path = os.path.abspath(config_path)
    complete_process(input_file, output_file, config_path)
    

if __name__ == "__main__":
    app()