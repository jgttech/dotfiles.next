import click
from pathlib import Path
from src.cfg import ProjectJson

@click.command("python")
def install() -> None:
    base = Path.cwd()
    project_json = ProjectJson.load(base)

    print(f"base: {base}")
    print(project_json.to_json())
