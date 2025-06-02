import click
from cli import cli

@click.command("version")
def main():
    print("VERSION")

cli.add_command(main)
