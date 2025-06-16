import src.cli as cli

@cli.command("zig")
def main(ctx: cli.Context) -> None:
    print("Uninstalling")
