import logging

logging.basicConfig(
    filename='shop.log',
    level=logging.DEBUG,
    format='%(name)s - %(levelname)s - %(funcName)s - %(message)s',
    filemode='a'
)
