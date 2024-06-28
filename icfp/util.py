from colorama import Fore, Style
from sys import stderr


def format_error(error: str) -> str:
    return Fore.RED + "Err: " + Style.RESET_ALL + error


def print_error(error: str) -> None:
    print(format_error(error), file=stderr)