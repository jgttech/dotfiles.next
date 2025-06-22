import src.cli as cli

@cli.command("python")
def main(ctx: cli.Context) -> None:
    env, conf = ctx.state

    print("[Environment]")
    print(f"home.....: {env.home}")
    print(f"bin......: {env.bin}")
    print(f"cfg......: {env.cfg}\n")
    print("[Conf]")
    print(f"packages.: {conf.packages}")
