from cmds.cli import cli
from src.os import build

@cli.command("version")
def main() -> None:
    print(build.version)
