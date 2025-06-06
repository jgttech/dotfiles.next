from pathlib import Path
from src.cfg import ProjectJson, BuildJson

class Context:
    project: ProjectJson
    build: BuildJson

    def __init__(self, base: Path, cli: Path) -> None:
        project = ProjectJson.load(base)
        build = BuildJson(project, base, base / cli)

        self.project = project
        self.build = build

    # Intented for any initialization work to
    # prep the installation process.
    def init(self) -> None:
        self.build.init()
