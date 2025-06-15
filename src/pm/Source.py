from abc import abstractmethod


class Source:
    @abstractmethod
    def install(self) -> None:
        """The function that handles creating the install command"""
        pass
