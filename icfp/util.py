from colorama import Fore, Style


def format_error(error: str) -> str:
    return Fore.RED + "Err: " + Style.RESET_ALL + error
