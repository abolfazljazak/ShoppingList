import os
import logging
from getpass import getpass
from difflib import SequenceMatcher
from shop.helper.type_hint import Product, Basket, Quantity
from shop.helper.exception import (
    ProductNameError,
    ProductDoesNotExist,
    SearchError
)

logger = logging.getLogger(__name__)


def similarity(actual, expected):
    return SequenceMatcher(None, actual, expected).ratio()


def search_basket(basket: Basket, keyword: str) -> None:
    print(f"Search for {keyword}...")
    results = [
        (product, similarity(product['name'], keyword))
        for product in basket
        if keyword.lower() in product['name'].lower()
    ]
    if results:
        print(f'Found ({len(results)}) results:')
        for product, score in results:
            print(f'Product: {product["name"]}, Similarity Score: {score:.2f}')
    else:
        raise SearchError("No result found.")


def select_item(products, item) -> Product | ProductDoesNotExist:
    for product in products:
        if product.name == item:
            selected_product = product
            break
    else:
        raise ProductDoesNotExist(f"Product {item} does not exist.")
    return selected_product


def add_item(basket: Basket, item: Product, number) -> Basket:
    logger.debug(f"Adding `{item}` to user's basket.")
    basket.append({'name': item.name, 'number': number, 'price': item.price})
    print(f'`{item.name}` is added to the basket.')
    return basket


def show_total_items(basket) -> None:
    print(f'now you have {len(basket)} items in the basket.')


def remove_item(basket: Basket, item: Product) -> Product:
    logger.debug(f"Removing `{item}` from user's basket.")
    if item in basket:
        basket.remove(item)
        print(f'{item} is removed from the basket.')
    else:
        logger.warning(f"Product {item} does not exist.")
        raise ProductDoesNotExist(f"Product {item} does not exist.")
    return item


def is_valid_item(item: Product, products, raise_exc: bool = False) -> bool | Exception:
    global message
    if not item:
        is_valid = False
        message = 'Product Must not be empty.'
    elif not item in products:
        is_valid = False
        message = 'Product Must be one of available products that shown to you.'
    else:
        is_valid = True

    if raise_exc and not is_valid:
        raise ProductNameError(message)
    else:
        return is_valid


def clear_screen():
    os.system("cls")


def show_help():
    print('----')
    print("Please enter a command when you see `>`.")
    print("Please write `add` to enter your product.")
    print("Please write `show` to show your product's of basket.")
    print("Please write `help` to show commands.")
    print("Please write `exit` to exit from your project.")
    print('----')


def show_error(message):
    print(f'Error: {message}!')
    getpass('Please enter to continue...')


def total_price_basket(basket: Basket, func):
    total_price = 0
    for product in basket:
        total_price += int(product['price']) * int(product['number'])
    apply_discount = func(total_price)
    print(f'total price>   ${apply_discount:.2f}')


def show_basket(basket: Basket) -> None:
    print("Your Basket:")
    for prod in basket:
        print(f"- {prod.name}, {prod.quantity}")


def apply_ten_discount(price: int) -> int:
    return price * 0.9


def apply_no_discount(price: int) -> int:
    return price


def paginator(basket: Basket, page_number: int, func):
    total_product = len(basket)
    if total_product > 0:
        if total_product % 5 == 0:
            total_page = total_product // 5
            func(basket, page_number, total_page)
            return total_page

        elif total_product % 5 != 0:
            total_page = (total_product // 5) + 1
            func(basket, page_number, total_page)
            return total_page


def paginate(basket: Basket, page_number, total_pages):
    start = (page_number - 1) * 5
    end = page_number * 5
    product = basket[start:end]

    for item in product:
        total_price = int(item['number']) * int(item['price'])
        print(f'product: {item["name"]}  quantity: {item["number"]}  price: {total_price}')

    if page_number > total_pages:
        print('"The entered page number is greater than the total number of pages."')

    elif not product:
        print('There is no product')
