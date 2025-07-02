from cmds.cli import cli
from cmds.version import main as version

cli.add_command(version)

def run() -> None:
    cli()
