import src.cli as cli

@cli.uninstall("go")
def main(ctx: cli.Context) -> None:
    print("Uninstalling")
