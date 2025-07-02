from subprocess import call
from cmds.cli import cli
from src.os import build

@cli.command("edit")
def main() -> None:
    call("nvim .", shell=True, cwd=build.home)
