import src.cli as cli

@cli.command("python")
def main(ctx: cli.Context) -> None:
    print("Uninstalling")
