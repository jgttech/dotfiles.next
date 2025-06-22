import src.cli as cli

@cli.install("zig")
def main(ctx: cli.Context) -> None:
    print("Installing")
