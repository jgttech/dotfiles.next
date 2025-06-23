from subprocess import call
import src.cli as cli

@cli.install("go")
def main(ctx: cli.Context) -> None:
    env, _ = ctx.state
    call(f"go build -o {env.bin / "dotfiles"} main.go", shell=True)

