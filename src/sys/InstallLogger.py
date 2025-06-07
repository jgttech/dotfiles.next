from rich.console import Console
from rich.status import Status

class InstallLogger:
    console: Console
    status: Status
    max: int

    def __init__(self, console: Console, status: Status, max: int) -> None:
        self.console = console
        self.status = status
        self.max = max

    def checking(self, current: int, name: str) -> None:
        string: list[str] = [
            f"[dim]{current + 1}/{self.max}[/dim]",
            f"Checking [bold cyan]{name}[/bold cyan],",
            "please wait..."
        ]

        self.status.update(" ".join(string))

    def installing(self, current: int, name: str) -> None:
        string: list[str] = [
            f"[dim]{current + 1}/{self.max}[/dim]",
            f"Installing [bold cyan]{name}[/bold cyan],",
            "please wait..."
        ]

        self.status.update(" ".join(string))

    def ok(self, name: str) -> None:
        string: list[str] = [
            f"[green]| ok |[/green]",
            f"[bold green]✔[/bold green]",
            f"[cyan]{name}[/cyan]"
        ]

        self.console.print(" ".join(string))

    def fail(self, name: str) -> None:
        string: list[str] = [
            f"[red]|fail|[/red]",
            f"[bold red]✘[/bold red]",
            f"[cyan]{name}[/cyan]"
        ]

        self.console.print(" ".join(string))
