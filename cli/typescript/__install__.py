import src.cli as cli

@cli.install("typescript")
def main(ctx: cli.Context) -> None:
    print("Installing")
