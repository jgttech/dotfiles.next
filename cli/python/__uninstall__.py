import src.cli as cli

@cli.uninstall("python")
def main(ctx: cli.Context) -> None:
    print("Uninstalling")
