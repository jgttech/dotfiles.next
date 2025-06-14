from os import getenv, path, access, X_OK
from subprocess import run, TimeoutExpired
from shutil import which


def installed(cmd: str) -> bool:
    where = which(cmd)

    if where:
        return True

    try:
        run([cmd, "--version"], capture_output=True, timeout=3)
        return True
    except (FileNotFoundError, TimeoutExpired):
        pass

    PATH = getenv("PATH", "/usr/bin:/usr/local/bin:/bin:/sbin").split(":")
    for dir in PATH:
        cmd_path = path.join(dir, cmd)

        if path.isfile(cmd_path) and access(cmd_path, X_OK):
            return True

    return False
