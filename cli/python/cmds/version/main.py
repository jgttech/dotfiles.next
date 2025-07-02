from cmds.cli import cli
from src.os import Build

@cli.command("version")
def main() -> None:
    build = Build()
    print(build.version)
