from shop.helper.type_hint import Basket, Product
from shop.helper.const import EXIT_COMMANDS
from shop.helper.exception import ProductDoesNotExist
from shop.utils.classes import Shopping
from shop.utils.funcs import (
    clear_screen,
    show_total_items,
    remove_item,
    show_error, logger
)


def handle_remove_command(basket: Basket):
    shopping = Shopping(basket)
    clear_screen()
    product: Product = input('(Remove)>> ')

    if product in EXIT_COMMANDS:
        return None
    try:
        shopping.remove_item(product)
        show_total_items(basket)

    except ProductDoesNotExist as e:
        show_error(e)

    except Exception as e:
        logger.critical(e, exc_info=True)
        show_error('500! please contact administrator.')
