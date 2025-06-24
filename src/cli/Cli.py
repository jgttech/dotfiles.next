from click import Group
from pathlib import Path
from importlib import import_module

class Cli:
    root: Path
    cli = Group()
    install = Group("install")
    uninstall = Group("uninstall")
    update = Group("update")

    def __init__(self, root: Path) -> None:
        self.root = root

        if not self.root.is_dir():
            raise FileNotFoundError(f"Directory does not exist: {self.root}")

        for cmd in self.root.iterdir():
            if not cmd.is_dir():
                continue

            name = f"{self.root.name}.{cmd.name}"
            install_module = import_module(f"{name}.__install__")
            uninstall_module = import_module(f"{name}.__uninstall__")
            update_module = import_module(f"{name}.__update__")

            if hasattr(install_module, "main"):
                self.install.add_command(install_module.main)

            if hasattr(uninstall_module, "main"):
                self.uninstall.add_command(uninstall_module.main)

            if hasattr(update_module, "main"):
                self.update.add_command(update_module.main)

    def run(self) -> None:
        self.cli.add_command(self.install)
        self.cli.add_command(self.uninstall)
        self.cli.add_command(self.update)
        self.cli()
