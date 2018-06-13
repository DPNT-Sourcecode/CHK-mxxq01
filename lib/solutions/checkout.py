from collections import defaultdict

sku_prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 70,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 20,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 17,
    'Y': 20,
    'Z': 21,
}

def __multiple_promo(basket, sku, count, price):
    promo_cost = 0
    offers = basket[sku] / count
    if offers > 0:
        promo_cost = offers * price
    basket[sku] -= offers * count
    return basket, promo_cost

def __get_some_free(basket, buy_sku, buy_count, free_sku):
    if buy_sku != free_sku:
        offers = basket[buy_sku] / buy_count
    else:
        offers = basket[buy_sku] / (buy_count + 1)
    if offers > 0:
        basket[free_sku] = max(0, basket[free_sku] - offers)
    return basket, 0

def __group_discount(basket, group, count, price):
    promo_cost = 0
    offers = sum([basket[sku] for sku in group]) / count
    if offers == 0:
        return basket, 0
    promo_cost = offers * price
    promo_skus = offers * count
    ordering = sorted([(sku, sku_prices[sku]) for sku in group], key=lambda k: k[1], reverse=True)
    for sku, _ in ordering:
        if promo_skus == 0:
            break
        to_remove = basket[sku] - promo_skus
        promo_skus = max(0, promo_skus - basket[sku])
        basket[sku] = max(0, to_remove)
    return basket, promo_cost

promotions = [
    lambda b: __group_discount(b, ['S', 'T', 'X', 'Y', 'Z'], 3, 45),
    lambda b: __get_some_free(b, 'E', 2, 'B'),
    lambda b: __get_some_free(b, 'F', 2, 'F'),
    lambda b: __get_some_free(b, 'N', 3, 'M'),
    lambda b: __get_some_free(b, 'R', 3, 'Q'),
    lambda b: __get_some_free(b, 'U', 3, 'U'),
    lambda b: __multiple_promo(b, 'A', 5, 200),
    lambda b: __multiple_promo(b, 'A', 3, 130),
    lambda b: __multiple_promo(b, 'B', 2, 45),
    lambda b: __multiple_promo(b, 'H', 10, 80),
    lambda b: __multiple_promo(b, 'H', 5, 45),
    lambda b: __multiple_promo(b, 'K', 2, 120),
    lambda b: __multiple_promo(b, 'P', 5, 200),
    lambda b: __multiple_promo(b, 'Q', 3, 80),
    lambda b: __multiple_promo(b, 'V', 3, 130),
    lambda b: __multiple_promo(b, 'V', 2, 90),
]

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    basket = defaultdict(lambda: 0)
    for sku in skus:
        if sku not in sku_prices.keys():
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

    return cost
