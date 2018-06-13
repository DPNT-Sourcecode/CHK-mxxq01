from collections import defaultdict

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

def __multiple_promo(basket, sku, count, price):
    promo_cost = 0
    sku_count = basket[sku]
    offers = sku_count / count
    if offers > 0:
        promo_cost = offers * price
    basket[sku] -= offers * count
    return basket, promo_cost

def promo_a_5(basket):
    return __multiple_promo(basket, 'A', 5, 200)

def promo_a_3(basket):
    return __multiple_promo(basket, 'A', 3, 130)

def promo_b_2(basket):
    return __multiple_promo(basket, 'B', 2, 45)

def promo_e_bfree(basket):
    e_count = basket['E']
    offers = e_count / 2
    if offers > 0:
        basket['B'] = max(0, basket['B'] - offers)
    return basket, 0

promotions = [
    promo_a_5,
    promo_a_3,
    promo_e_bfree,
    promo_b_2,
]

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    basket = defaultdict(lambda: 0)
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
