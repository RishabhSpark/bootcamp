import typer
from rishabh_hello.hello import hello

app = typer.Typer()

@app.command()
def greet(name: str = typer.Option("World", help="Name to greet")):
    hello(name)

if __name__ == "__main__":
    app()