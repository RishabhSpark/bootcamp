import typer
import yaml
from router import StateBasedRouter

app = typer.Typer()

def read_lines(path: str):
    with open(path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def read_config(path: str):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

@app.command()
def process(
    input_file: str = typer.Option(..., "--input", "-i", help="Path to the input file"),
    config_path: str = typer.Option("config.yaml", "--config", "-c", help="Path to the pipeline config file"),
):
    """
    Process the input file and write the output to a file or print it.
    """

    router = StateBasedRouter(read_config(config_path))
    router.run('start', read_lines(input_file))

if __name__ == "__main__":
    app()