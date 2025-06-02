from pathlib import Path
import src.cli as cli

if __name__ == "__main__":
    app = cli.App(root=Path.cwd() / "cmds")
    app.run()
