from sys import platform
from pathlib import Path
from src.os import Build
from src.env import env

def create_build() -> None:
    build = Build()
    os_packages: list[Path] = []
    os_path = Path(build.home) / "os"
    platform_path = os_path / platform
    shared_path = os_path / "shared"

    if not os_path.exists():
        raise FileNotFoundError(os_path)
        
    if not shared_path.exists():
        raise FileNotFoundError(shared_path)

    if not platform_path.exists():
        raise FileNotFoundError(platform_path)

    for dir in shared_path.iterdir():
        os_packages.append(dir)

    for dir in platform_path.iterdir():
        os_packages.append(dir)

    build.os = os_packages

    with open(env.build_file, "w") as file:
        file.write(build.to_json())
