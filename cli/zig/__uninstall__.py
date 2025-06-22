import src.cli as cli

@cli.uninstall("zig")
def main(ctx: cli.Context) -> None:
    print("Uninstalling")
