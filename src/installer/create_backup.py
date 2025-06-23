from pathlib import Path
from os import rename
from src.os import Build

def create_backup() -> None:
    build = Build()
    zshrc = Path.home() / ".zshrc"

    if zshrc.exists():
        rename(zshrc, build.zshrc_backup)
