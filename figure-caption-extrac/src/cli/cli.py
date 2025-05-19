import typer
from src.cli.commands.ingest import ingest_app
from src.cli.commands.export import export_app
from src.cli.commands.watch import watch_app
from src.cli.commands.config import config_app

app = typer.Typer(help="Figure Caption Extraction CLI")
app.add_typer(ingest_app, name="ingest")
app.add_typer(export_app, name="export")
app.add_typer(watch_app, name="watch")
app.add_typer(config_app, name="config")

if __name__ == "__main__":
    app()