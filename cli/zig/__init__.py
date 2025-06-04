import click

@click.command("zig")
def install() -> None:
    print("Installing zig")
