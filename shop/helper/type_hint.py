from typing import NewType

Product = NewType('Product', str)
Quantity = NewType('Quantity', int)
Price = NewType('Price', int)
Basket = NewType('Basket', list[Product])



