from pathlib import Path
from subprocess import call
from src.os import Build

def create_links() -> None:
    build = Build()
    dirs: set[Path] = set[Path]()

    for link in build.os:
        dirs.add(link.parent)

    for dir in dirs:
        stow = f"stow -t {Path.home()}"
        pkgs: set[str] = set[str]()

        for sub in dir.iterdir():
            pkgs.add(sub.name)

        stow = " ".join([stow, " ".join(pkgs)])
        call(stow, shell=True, cwd=dir)
