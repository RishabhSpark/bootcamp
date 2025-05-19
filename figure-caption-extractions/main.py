import sys

def start_cli():
    from src.cli.cli import app as cli_app
    cli_app()

def start_api():
    import uvicorn
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "fastapi":
        start_api()
    else:
        start_cli()