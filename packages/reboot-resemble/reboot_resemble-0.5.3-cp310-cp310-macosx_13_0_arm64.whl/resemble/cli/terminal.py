"""Tooling to interact with a command-line terminal"""

import colorama
import sys
from colorama import Fore, Style
from resemble.aio.once import Once
from typing import NoReturn


def init():
    colorama_init_once = Once(colorama.init)
    colorama_init_once()


# TODO(benh): move these helpers into a generic "CLI" module.
def info(message: str):
    if sys.stdout.isatty():
        print(
            Fore.GREEN + Style.BRIGHT + message + Style.RESET_ALL,
            file=sys.stdout,
        )
    else:
        print(message, file=sys.stdout)


def warn(message: str):
    if sys.stdout.isatty():
        print(
            Fore.YELLOW + Style.BRIGHT + message + Style.RESET_ALL,
            file=sys.stdout,
        )
    else:
        print(message, file=sys.stdout)


def error(message: str):
    if sys.stderr.isatty():
        print(
            Fore.RED + Style.BRIGHT + message + Style.RESET_ALL,
            file=sys.stderr,
        )
    else:
        print(message, file=sys.stderr)


def fail(message: str) -> NoReturn:
    error(message)
    sys.exit(1)
