import logging

from conf import *
from shop.helper.type_hint import Basket
from shop.utils.funcs import clear_screen, show_help
from shop.utils.command import COMMANDS
from shop.helper.const import (
    RUNNING,
    EXIT_COMMANDS
)

logger = logging.getLogger(__name__)


def main():
    clear_screen()
    print("Welcome...")

    basket: Basket = list()

    show_help()

    while RUNNING:
        command = input('> ').lower()

        if command in EXIT_COMMANDS:
            break
        elif command in COMMANDS:
            clear_screen()
            execute_action = COMMANDS[command]
            execute_action(basket)

        else:
            raise NotImplementedError()
