import click
from sys import platform
from os import path
from pathlib import Path
from src.cfg import Build, Project
from src.sys import timestamp

@click.command("install")
@click.option("--root", help="The base directory where the dotfiles will live.")
def main(root: str) -> None:
    home = Path(root)
    created_at = timestamp()
    zshrc_backup = Path.home() / f"zshrc.{created_at}.backup"

    project = Project.load(home)
    stow = home / project.stow
    cli = home / project.cli
    out = home / project.out
    cfg = out / project.cfg
    bin = out / project.bin

    build = Build(
        version=project.version,
        home=str(home),
        stow=str(stow),
        cli=str(cli),
        cfg=str(cfg),
        bin=str(bin),
        out=str(out),
        zshrc_backup=str(zshrc_backup),
        created_at=created_at,
        packages=[]
    )

    for dir in stow.iterdir():
        if dir.name == "shared":
            for sub in dir.iterdir():
                build.packages.append(path.join("shared", sub.name))

        if dir.name == platform:
            for sub in dir.iterdir():
                build.packages.append(path.join(platform, sub.name))

    out.mkdir(parents=True, exist_ok=True)
    cfg.mkdir(parents=True, exist_ok=True)
    bin.mkdir(parents=True, exist_ok=True)
