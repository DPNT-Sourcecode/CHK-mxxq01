# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+

sku_prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
}

promotions = {
    'A': {
        'quantity': 3,
        'price': 130,
    },
    'B': {
        'quantity': 2,
        'price': 45,
    }
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    raise NotImplementedError()
