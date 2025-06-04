import click
from pathlib import Path
from importlib import import_module
from src.errors import ModuleNotFound

class Cli:
    root: Path
    cli: click.Group
    install: click.Group

    def __init__(self, root: Path) -> None:
        self.root = root
        self.cli = click.Group()

        install = click.Group("install")

        # Register all the commands that exist.
        if self.root.is_dir():
            for cmd in self.root.iterdir():
                if not cmd.is_dir:
                    return

                name = f"{self.root.name}.{cmd.name}"
                module = import_module(name)

                if not hasattr(module, "install"):
                    raise ModuleNotFoundError(name)

                install.add_command(module.install)

        self.install = install

    def run(self) -> None:
        self.cli.add_command(self.install)
        self.cli()
