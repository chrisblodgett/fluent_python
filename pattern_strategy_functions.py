"""Implementing the classic Strategy Design Pattern using Functions and Decorators, rather than classes and objects"""

from abc import abstractmethod
from collections.abc import Sequence
from decimal import Decimal
from typing import Callable  # optional is the same as Union[x, None]
from typing import NamedTuple, Optional


class Customer(NamedTuple):
    name: str
    fidelity: int


class LineItem(NamedTuple):
    product: str
    quantity: int
    price: Decimal

    def total(self) -> Decimal:
        return self.quantity * self.price


class Order(NamedTuple):
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional[Callable[['Order'], Decimal]] = (
        None  # now we can provide a callable (function) to be tied
    )

    def total(self) -> Decimal:
        totals = (
            item.total() for item in self.cart
        )  # call the total() of each LineItem object
        return sum(totals, start=Decimal(0))  # sum up all the totals start with 0

    def due(self) -> Decimal:
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self) -> str:
        return f"order total {self.total():.2f} due {self.due():.2f}"


# make a couple promotion functions


def large_order_promo(order: Order) -> Decimal:
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal(
                '0.1'
            )  # 10% discount on each item price that has >= 20 items bought
    return discount


def fidelity_promo(order: Order) -> Decimal:
    if order.customer.fidelity >= 1000:
        return order.total() * Decimal('0.05')
    return Decimal(0)


ming = Customer('ming', 1000)
cart = [LineItem('banana', 4, Decimal(0.5)), LineItem('orange', 8, Decimal('1.5'))]
cart2 = [LineItem('banana', 22, Decimal(0.5)), LineItem('orange', 8, Decimal('1.5'))]

my_ord = Order(ming, cart, fidelity_promo)
my_ord2 = Order(ming, cart2, large_order_promo)
print(my_ord)
print(my_ord2)
