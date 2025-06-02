from dataclasses import dataclass, field
from dataclasses_json import DataClassJsonMixin

@dataclass
class Build(DataClassJsonMixin):
    # The version of the dotfiles when the build
    # was created.
    version: str = ""

    # The home directory for the dotfiles. This points
    # to where the source code is.
    home: str = ""

    # The directory of the tools that are in use for
    # the dotfiles CLI.
    cli: str = ""

    # The directory used to find the resources I want
    # to link within the users file system.
    stow: str = ""

    # The directory where all the build output goes.
    out: str = ""

    # The config directory in the build directory.
    cfg: str = ""

    # The bin directory in the build directory.
    bin: str = ""

    # The ZSHRC config file that was replaced when
    # the dotfiles where installed. This helps in
    # reversing the ZSHRC config when an uninstall
    # is run.
    zshrc_backup: str = ""

    # When the build was created (unix timestamp).
    created_at: int = 0

    # The packages that are installed from the
    # dotfiles.
    packages: list[str] = field(default_factory=list)

    def save(self) -> None:
        pass
