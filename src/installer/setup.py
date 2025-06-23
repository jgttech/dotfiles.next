from src.env import env

def setup() -> None:
    bin = env.bin
    cfg = env.cfg

    if not bin.exists():
        bin.mkdir(parents=True)

    if not cfg.exists():
        cfg.mkdir(parents=True)
