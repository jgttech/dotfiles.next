import src.cli as cli

@cli.install("odin")
def main(ctx: cli.Context) -> None:
    print("Installing")
