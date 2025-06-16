from abc import abstractmethod


class Source:
    @abstractmethod
    def install(self, packages: list[str]) -> None:
        """The function that handles creating the install command"""
        pass
