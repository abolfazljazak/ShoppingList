import re
import logging
from shop.helper.exception import ProductDoesNotExist, DuplicateProductError
from shop.helper.type_hint import Basket, Product

logger = logging.getLogger(__name__)


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not re.match('[a-zA-Z\d]{8,}', value):
            raise Exception('invalid password')

        else:
            self.__password = value

    def login(self, username, password):
        if self.username == username and self.password == password:
            return True

        else:
            raise Exception('credentials wrong')


class Shopping:
    def __init__(self, basket: Basket):
        self.basket = basket

    def add_item(self, item: Product, number: int):
        """
        Adds an item to the user's basket.

        Args:
            item (Product): The product to add to the basket.
            number (int): The quantity of the product to add.

        Returns:
            None
        """
        if item in self.basket:
            logger.warning(f'This is a duplicate {item.name}')
            raise DuplicateProductError(f'This is a duplicate {item.name}')

        else:
            logger.debug(f"Adding `{item.name}` to user's basket.")
            self.basket.append({'name': item.name, 'number': number, 'price': item.price})
            print(f'`{item.name}` is added to the basket.')
            return self.basket

    def remove_item(self, item: Product):
        """
            Removes an item from the user's basket.

            Args:
                basket (Basket): The user's basket.
                item (Product): The product to remove from the basket.

            Returns:
                Product: The removed product.

            Raises:
                ProductDoesNotExist: If the product does not exist in the basket.
            """

        logger.debug(f"Removing `{item}` from user's basket.")
        for i in self.basket:
            if item == i['name']:
                self.basket.remove(i)
                logger.debug(f"{item} is removed from the basket.")
                print(f'{item} is removed from the basket.')
                return self.basket

        raise ValueError(f"The item '{item}' does not exist in the basket.")

    def total_price_basket(self, func):
        logger.debug('Calculating the total price of the items in the basket.')
        total_price = 0
        for item in self.basket:
            total_price += int(item['price']) * int(item['number'])

        apply_discount = func(total_price)

        if apply_discount < 0:
            raise ValueError('The discount function returned a negative value.')

        print(f'Total price: ${apply_discount:.2f}')
        logger.debug('The final price was displayed')

    def paginator(self, page_number):
        """
            Paginates a list of products and applies a function to the selected page.

            Args:
                page_number (int): The page number to retrieve.

            Returns:
                The result of applying the function to the selected page.

            Raises:
                ValueError: If the pagination values are invalid.
                Exception: If an unknown error occurs.
            """
        page_size = 5
        total_page = 0
        total_products = len(self.basket)
        if total_products > page_size > 0:
            if total_products % page_size == 0:
                total_page += total_products // page_size

            else:
                total_page += (total_products // page_size) + 1

        start = (page_number - 1) * 5
        end = page_number * 5
        product = self.basket[start:end]

        for item in product:
            total_price = int(item['number']) * int(item['price'])
            print(f'product: {item["name"]}  quantity: {item["number"]}  price: {total_price}')

        if page_number > total_page:
            print('"The entered page number is greater than the total number of pages."')

        elif not product:
            print('There is no product')

        elif total_products < page_size or page_size < 0:
            logger.debug('The user did not enter the correct pagination value')
            raise ValueError('Enter the correct value for pagination')

        else:
            logger.warning('Invalid pagination values entered by the user')
            raise Exception('Unknown error occurred while paginating products')

        return total_page

    def show_total_items(self) -> None:
        """
        Displays the total number of items in the basket.
        """
        logger.debug("Calculating the total number of items in the basket.")
        total_items = len(self.basket)
        print(f"Now you have {total_items} items in the basket.")

    @staticmethod
    def select_item(products, item) -> Product | ProductDoesNotExist:
        """
        Selects a product from a list of products based on its name.

        Args:
            products (list): The list of products to search in.
            item (str): The name of the product to select.

        Returns:
            The selected product.

        Raises:
            ProductDoesNotExist: If the specified product does not exist.
        """
        logger.debug(f"Selecting product: {item}")

        for product in products:
            if product.name == item:
                selected_product = product
                logger.debug(f"Product {item} selected: {selected_product}")
                break
        else:
            logger.warning(f"Product {item} does not exist.")
            raise ProductDoesNotExist(f"Product {item} does not exist.")

        return selected_product
