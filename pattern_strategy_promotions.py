""" for strategy pattern you can include all of the modules here then include 
them by using best_promo"""

from decimal import Decimal
from typing import Callable

from pattern_strategy_functions import Customer, LineItem, Order

Promotion = Callable[[Order], 'Decimal']
promos: list[Promotion] = []


def promotion(promo: Promotion) -> Promotion:
    """this decorator function will add the promotion to the list of promos so we can use best_promo"""
    promos.append(promo)
    return promo


def best_promo(order: Order) -> Decimal:
    best = max(
        promo(order) for promo in promos
    )  # loop through promos and pass in order and see which gives the best discount
    return best


@promotion
def large_order_promo(order: Order) -> Decimal:
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal(
                '0.10'
            )  # 10% discount on each item price that has >= 20 items bought
    return discount


@promotion
def fidelity_promo(order: Order) -> Decimal:
    if order.customer.fidelity >= 1000:
        return order.total() * Decimal('0.05')
    return Decimal(0)


ming = Customer('ming', 1000)
cart = [LineItem('orange', 30, Decimal('1.0'))]
cart2 = [LineItem('banana', 22, Decimal(0.5)), LineItem('orange', 8, Decimal('1.5'))]

order1 = Order(ming, cart, best_promo)
print(order1)
