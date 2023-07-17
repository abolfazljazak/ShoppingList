import random
import re

from collections import namedtuple

Product = namedtuple('Product', ['name', 'price', 'in_stock', 'quantity', 'number'])

product_list = ['apple',
                'watermelon',
                'orange',
                'pear',
                'cherry',
                'grape',
                'strawberry',
                'mango',
                'blueberry',
                'Pomegranate',
                'plum',
                'banana',
                'raspberry',
                'kiwi',
                'papaya',
                'pineapple',
                'lime',
                'lemon',
                'melon',
                'coconut',
                'avocado',
                'peach',
                ]

products = [
    Product(name=i,
            price=random.randint(10, 250),
            in_stock=random.choice([True, False]),
            quantity=random.randint(10, 20),
            number=None
            )
    for i in product_list
]


def get_all_products():
    return products


def get_available_products():
    prods = list(filter(lambda prod: prod.in_stock, products))
    return prods

# while True:
#     username = input('username: ')
#     password = input('password: ')
#
#     try:
#         user = User(username, password)
#         print('successfully')
#         break
#
#     except Exception as e:
#         print(e)
#
#
# while True:
#     username1 = input('username: ')
#     password1 = input('password: ')
#
#     try:
#         if user.login(username1, password1):
#             print('logged in')
#             break
#
#     except Exception as e:
#         print(e)
