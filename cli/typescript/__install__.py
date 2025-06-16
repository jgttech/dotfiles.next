import src.cli as cli

@cli.command("typescript")
def main(ctx: cli.Context) -> None:
    print("Installing")
