from typing import Optional
from rich import print

def hello(name: Optional[str] = 'World') -> None:
    print(f"[blue]Hello, [cyan]{name}[cyan]![/blue]")