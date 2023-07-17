from shop.helper.type_hint import Basket
from shop.helper.const import (
    RUNNING,
    EXIT_COMMANDS,
)
from shop.utils.classes import Shopping
from shop.utils.funcs import (
    clear_screen,
    paginator,
    paginate,
)


def handle_show_command(basket: Basket):
    shopping = Shopping(basket)

    while RUNNING:

        page_number = input('Enter the desired page: ')

        if page_number in EXIT_COMMANDS:
            clear_screen()
            break

        else:
            clear_screen()
            page_number = int(page_number)
            total_page = shopping.paginator(page_number)
            if 0 < page_number <= int(total_page):
                print(f'page: {page_number}/{total_page}')
