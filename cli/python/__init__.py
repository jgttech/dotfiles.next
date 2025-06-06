import src.cli as cli

@cli.installer("python")
def install(ctx: cli.Context) -> None:
    print(ctx.project.to_json())
    print(ctx.build.to_json())
