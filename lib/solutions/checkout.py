from collections import defaultdict

# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      |
# | G    | 20    |                        |
# | H    | 10    | 5H for 45, 10H for 80  |
# | I    | 35    |                        |
# | J    | 60    |                        |
# | K    | 80    | 2K for 150             |
# | L    | 90    |                        |
# | M    | 15    |                        |
# | N    | 40    | 3N get one M free      |
# | O    | 10    |                        |
# | P    | 50    | 5P for 200             |
# | Q    | 30    | 3Q for 80              |
# | R    | 50    | 3R get one Q free      |
# | S    | 30    |                        |
# | T    | 20    |                        |
# | U    | 40    | 3U get one U free      |
# | V    | 50    | 2V for 90, 3V for 130  |
# | W    | 20    |                        |
# | X    | 90    |                        |
# | Y    | 10    |                        |
# | Z    | 50    |                        |
# +------+-------+------------------------+

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
    'K': 80,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 30,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 90,
    'Y': 10,
    'Z': 50,
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

def promo_f_ffree(basket):
    f_count = basket['F']
    offers = f_count / 3
    if offers > 0:
        basket['F'] = max(0, basket['F'] - offers)
    return basket, 0

promotions = [
    promo_a_5,
    promo_a_3,
    promo_e_bfree,
    promo_b_2,
    promo_f_ffree,
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
