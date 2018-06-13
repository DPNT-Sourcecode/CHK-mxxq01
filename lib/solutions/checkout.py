# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+

sku_prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
}

def promo_a_3(basket):
    promo_cost = 0
    return basket, promo_cost

def promo_a_5(basket):
    promo_cost = 0
    return basket, promo_cost

def promo_e_bfree(basket):
    promo_cost = 0
    return basket, promo_cost

promotions = [
    promo_a_5,
    promo_a_3,
    promo_e_bfree,
]

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    basket = {}
    for sku in skus:
        if sku not in sku_prices:
            return -1
        if sku not in basket:
            basket[sku] = 0
        basket[sku] += 1

    cost = 0
    for promo in promotions:
        basket, promo_cost = promo(basket)
        cost += promo_cost
    for sku, count in basket.items():
        cost += count * sku_prices[sku]

        # if sku in promotions.keys() and count / promotions[sku]['quantity'] != 0:
        #     cost += (count / promotions[sku]['quantity']) * promotions[sku]['price']
        #     cost += (count % promotions[sku]['quantity']) * sku_prices[sku]
        # else:
        #     cost += count * sku_prices[sku]

    return cost
