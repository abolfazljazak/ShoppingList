from shop.helper.exception import SearchError
from shop.helper.type_hint import Basket, Product
from shop.helper.const import EXIT_COMMANDS
from shop.utils.funcs import (
    clear_screen,
    search_basket, show_error,
)


def handle_search_command(basket: Basket):
    clear_screen()
    keyword: str = input('(Search)>> ')
    if keyword in EXIT_COMMANDS:
        return None
    try:
        search_basket(basket, keyword)

    except SearchError as e:
        show_error(e)
