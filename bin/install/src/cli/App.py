import click
from pathlib import Path
from importlib import import_module

class App:
    root: Path
    cli: click.Group

    def __init__(self, root: Path) -> None:
        self.root = root
        self.cli = click.Group()

        # Register all the commands that exist.
        if self.root.is_dir():
            for cmd in self.root.iterdir():
                file = cmd / "__cli__.py"

                if not cmd.is_dir and not file.exists():
                    return

                name = f"{self.root.name}.{cmd.name}.{file.stem}"
                module = import_module(name)

                if not hasattr(module, "main"):
                    print(f"ERROR: Failed to load module: {name}")
                    return

                self.cli.add_command(module.main)

    def run(self) -> None:
        # Run the CLI app.
        self.cli()
