from dataclasses_json import DataClassJsonMixin
from dataclasses import dataclass, field
from pathlib import Path
from json import load
from rich.console import Console
from src.env import DOTFILES_CONFIG_JSON
from src.errors import FileNotFound
from src.sys import InstallLogger
from src.pm import Package

@dataclass
class ProjectJson(DataClassJsonMixin):
    version: str = ""
    out: str = ""
    cfg: str = ""
    bin: str = ""
    dependencies: dict[str, str] = field(default_factory=dict)

    @staticmethod
    def load(dir: Path):
        file = dir / DOTFILES_CONFIG_JSON

        if not file.exists():
            raise FileNotFound(file)

        with open(file, "r") as ref:
            return ProjectJson.from_dict(load(ref))

    def ensure_dependencies(self) -> None:
        console = Console()
        max = len(self.dependencies)

        print(self.dependencies)
        console.print("[bold]Checking dependencies, please wait...[/bold]")

        with console.status("Please wait...") as status:
            log = InstallLogger(console, status, max)

            for idx, name in enumerate(self.dependencies):
                value = self.dependencies[name]
                pkg = Package(name)

                log.checking(idx, pkg.name)

                if value == "auto":
                    if pkg.exists():
                        log.ok(name)
                    else:
                        log.installing(idx, name)
                        pkg.install()

                        if pkg.exists():
                            log.ok(name)
                        else:
                            log.fail(name)
                    
        console.print("[dim bold]Done.[/dim bold]")
