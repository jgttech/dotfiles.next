import src.cli as cli

@cli.uninstall("typescript")
def main(ctx: cli.Context) -> None:
    print("Uninstalling")
