class ShopError(Exception):
    pass


class ProductDoesNotExist(ShopError):
    pass


class ProductNameError(ShopError):
    pass


class DuplicateProductError(ShopError):
    pass


class SearchError(ShopError):
    pass
