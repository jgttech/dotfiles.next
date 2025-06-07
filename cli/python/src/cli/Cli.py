import click
from pathlib import Path
from importlib import import_module
from src.errors import ModuleNotFound

class Cli:
    root: Path
    cli: click.Group

    def __init__(self, dir: str) -> None:
        print(dir)

    def run(self) -> None:
        self.cli()
