import logging

from shop.utils.classes import Shopping
from shop.models import get_available_products
from shop.helper.type_hint import Basket, Product, Quantity
from shop.helper.const import EXIT_COMMANDS
from shop.helper.exception import ProductNameError, ProductDoesNotExist
from shop.utils.funcs import (
    add_item,
    is_valid_item,
    clear_screen,
    show_total_items,
    select_item,
    show_error,
)

logger = logging.getLogger(__name__)


def handle_add_command(basket: Basket):
    shopping = Shopping(basket)
    clear_screen()
    adding_state = True
    products = get_available_products()

    while adding_state:
        print("To exit adding items please press `q`.")

        for index, product in enumerate(products, start=1):
            print(f'{index}) {product.name}    ${product.price}   quantity: {product.quantity}')
        product: Product = input('(Add)>> ')
        if product not in EXIT_COMMANDS:
            quantity: Quantity = input('(number)>> ')

        clear_screen()

        if product in EXIT_COMMANDS:
            break

        elif not product:
            continue

        else:

            try:
                # selected_product = select_item(products, product)
                selected_product = shopping.select_item(products, product)
                is_valid_item(selected_product, products, raise_exc=True)
                # basket = add_item(basket, selected_product, quantity)
                basket = shopping.add_item(selected_product, int(quantity))
                show_total_items(basket)
            except ProductNameError as e:
                show_error(e)
            except ProductDoesNotExist as e:
                show_error(e)
            except Exception as e:
                logger.critical(e, exc_info=True)
                show_error('500! please contact administrator.')
