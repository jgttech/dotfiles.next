import click
from pathlib import Path
from src.cfg import ProjectJson, BuildJson

@click.command("python")
def install() -> None:
    base = Path.cwd()
    project_json = ProjectJson.load(base)
    build_json = BuildJson(base)

    print(f"base: {base}")
    print(project_json.to_json())
    print(build_json.to_json())
