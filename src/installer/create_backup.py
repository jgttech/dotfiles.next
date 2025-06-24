from pathlib import Path
from os import rename
from src.os import Build

def create_backup() -> None:
    HOME = Path.home()
    build = Build()
    zshrc = HOME / ".zshrc"
    zshrc_backup = HOME / build.zshrc_backup

    if zshrc.exists():
        rename(zshrc, zshrc_backup)
