from pathlib import Path
from subprocess import call
from src.os import Build
from src.env import env

def create_links() -> None:
    build = Build()
    cwd = env.cfg.parent
    dirs: set[Path] = set[Path]()
    HOME = Path.home()

    for link in build.os:
        dirs.add(link.parent)

    for dir in dirs:
        stow: list[str] = [f"stow -t {HOME}"]

        for sub in dir.iterdir():
            stow.append(sub.name)

        call(" ".join(stow), shell=True, cwd=dir)

    call(f"stow -t {HOME} {env.cfg.name}", shell=True, cwd=cwd)
