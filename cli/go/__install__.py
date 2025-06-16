import src.cli as cli

@cli.command("go")
def main(ctx: cli.Context) -> None:
    print("Installing")

