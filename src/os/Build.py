from time import time
from pathlib import Path
from json import dumps, load
from src.env import env
from src.conf import conf


class Build:
    name: str = conf.name
    version: str = conf.version
    home: Path = env.home
    build: Path = env.build
    bin: Path = env.bin
    cfg: Path = env.cfg
    zshrc_backup: Path = Path.home() / f".zshrc.{str(int(time()))}.backup"
    os: list[Path] = []

    def __init__(self) -> None:
        if not env.build_file.exists():
            return

        with open(env.build_file, "r") as file:
            data = load(file)
            self.name = data["name"]
            self.version = data["version"]
            self.home = Path(data["home"])
            self.build = self.home / data["build"]
            self.bin = self.home / data["bin"]
            self.cfg = self.home / data["cfg"]
            self.os = []
            
            for cfg in data["os"]:
                self.os.append(self.home / cfg)

    def to_json(self) -> str:
        return dumps({
            "name": self.name,
            "version": self.version,
            "home": str(self.home),
            "build": str(self.build.relative_to(self.home)),
            "bin": str(self.bin.relative_to(self.home)),
            "cfg": str(self.cfg.relative_to(self.home)),
            "zshrc_backup": str(self.zshrc_backup),
            "os": [*map(lambda p: str(p.relative_to(self.home)), self.os)],
        }, indent=2)
