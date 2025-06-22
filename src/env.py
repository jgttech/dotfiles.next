from typing import Optional
from pathlib import Path
from src.cli import MODE

class Environment:
    # The home/root/base directory of the
    # dotfiles.
    home: Path

    # The path to the build root directory.
    build: Path

    # The path to the builds "bin" directory.
    bin: Path

    # The path to the builds "cfg" directory.
    cfg: Path

    # Name of the config file at the root.
    conf_file: Path

    # What mode the environment is in.
    mode: Optional[MODE] = None

    def __init__(self) -> None:
        self.home = Path.cwd()
        self.build = self.home / ".build"
        self.cfg = self.build / "cfg"
        self.bin = self.build / "bin"
        self.conf_file = self.home / "dotfiles.yml"

env = Environment()
