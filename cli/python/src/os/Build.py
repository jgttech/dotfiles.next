import json
from pathlib import Path

class Build:
    name: str
    version: str
    home: Path
    build: Path
    bin: Path
    cfg: Path
    zshrc_backup: Path
    source: Path
    lang: str
    os: list[Path]

    def __init__(self) -> None:
        cfg = Path.home() / ".dotfiles.build.json"
        self.os = []

        with open(cfg, "r") as file:
            data = json.load(file)

            self.name = data["name"]
            self.version = data["version"]
            self.home = Path(data["home"])
            self.build = self.home / data["build"]
            self.bin = self.home / data["bin"]
            self.cfg = self.home / data["cfg"]
            self.zshrc_backup = Path.home() / data["zshrc_backup"]
            self.source = self.home / data["source"]
            self.lang = data["lang"]

            for pkg in data["os"]:
                self.os.append(self.home / pkg)

build = Build()
