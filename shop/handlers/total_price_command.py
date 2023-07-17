import logging

from shop.utils.classes import Shopping
from shop.utils.funcs import (
    total_price_basket,
    clear_screen,
    apply_ten_discount,
    apply_no_discount, show_error,
)
from shop.helper.const import CODE_DISCOUNT, EXIT_COMMANDS
from shop.helper.type_hint import Basket

logger = logging.getLogger(__name__)


def handle_total_price_command(basket: Basket):
    shopping = Shopping(basket)
    clear_screen()
    discount = input('Enter your discount code, if you dont have one, enter No: ').lower()
    if discount in CODE_DISCOUNT:
        try:
            shopping.total_price_basket(apply_ten_discount)
            logger.debug('The user used the discount code')
        except ValueError as e:
            show_error(str(e))

    elif discount == 'no':
        try:
            shopping.total_price_basket(apply_no_discount)
            logger.debug('The user did not use the discount code')
        except ValueError as e:
            show_error(str(e))

    elif discount in EXIT_COMMANDS:
        pass

    else:
        show_error('The entered value is not correct')