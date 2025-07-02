from cmds.cli import cli
from cmds.version import main as version
from cmds.edit import main as edit

cli.add_command(version)
cli.add_command(edit)

def run() -> None:
    cli()
