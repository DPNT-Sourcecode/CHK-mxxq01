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
    basket = {}
    for sku in skus:
        if sku not in basket:
            basket[sku] = 0
        basket[sku] += 1

    cost = 0
    for sku, count in basket.items():
        if sku in promotions.keys() and count / promotions[sku]['quantity'] != 0:
            cost += (count / promotions[sku]['quantity']) * promotions[sku]['price']
            cost += (count % promotions[sku]['quantity']) * sku_prices[sku]
        else:
            cost += count * sku_prices[sku]

    return cost
