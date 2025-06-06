import json
from pathlib import Path
from dataclasses import dataclass, field
from dataclasses_json import DataClassJsonMixin
from src.cfg.ProjectJson import ProjectJson
from src.sys import timestamp

@dataclass
class BuildJson(DataClassJsonMixin):
    # Unix build timestamp.
    created_at: int = timestamp()

    # Version from the DOTFILES_CONFIG_JSON file.
    version: str = ""

    # The home directory for the dotfiles source.
    base: str = ""

    # The directory of the CLI being used.
    cli: str = ""

    # Where the system resources are linked from.
    stow: str = ""

    # The base directory where the build output is.
    out: str = ""

    # The config path within the build output.
    cfg: str = ""

    # The bin path within the build output.
    bin: str = ""

    # The name of the original .zshrc file.
    zshrc_backup: str = ""

    # What os resources where linked in the build.
    packages: list[str] = field(default_factory=list)

    def __init__(self, project: ProjectJson, dir: Path, cli: Path) -> None:
        super().__init__()

        out = dir / ".build"
        cfg = out / "cfg"
        bin = out / "bin"

        cfg.mkdir(parents=True, exist_ok=True)
        bin.mkdir(parents=True, exist_ok=True)

        self.version = project.version
        self.base = str(dir)
        self.cli = str(cli)
        self.out = str(out)
        self.cfg = str(cfg)
        self.bin = str(bin)
        self.packages = []

    def init(self):
        Path(self.cfg).mkdir(parents=True, exist_ok=True)
        Path(self.bin).mkdir(parents=True, exist_ok=True)

    def save(self, to: Path) -> None:
        with open(to, "w") as file:
            file.write(json.dumps(self.to_dict(), indent=2))
