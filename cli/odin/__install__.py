import src.cli as cli

@cli.command("odin")
def main(ctx: cli.Context) -> None:
    print("Installing")
