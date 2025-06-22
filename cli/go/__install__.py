import src.cli as cli

@cli.install("go")
def main(ctx: cli.Context) -> None:
    print("Installing")

