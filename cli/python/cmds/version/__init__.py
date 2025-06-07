import src.cli as cli

@cli.command("version")
def main(ctx: cli.Context) -> None:
    print("VERSION")
