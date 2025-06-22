import src.cli as cli

@cli.uninstall("odin")
def main(ctx: cli.Context) -> None:
    print("Uninstalling")
