import typer
from pathlib import Path
from src.config.config_loader import load_config

config_app = typer.Typer(help="Config management")

@config_app.command("show")
def show(
    config_path: Path = typer.Option(None, help="Path to config YAML file")
):
    """
    Show current config settings
    """
    config = load_config(config_path)
    typer.echo(config.model_dump_json(indent=2))