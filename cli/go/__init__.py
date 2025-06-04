import click

@click.command("go")
def install() -> None:
    print("Installing go")
