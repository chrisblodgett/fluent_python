"""
    we can call iter() with with a callable to keep getting invoked repeadtly 
    until a condition is met"""

import typing
from random import randint


def d6():
    return randint(1, 6)


# print(d6())
i = iter(
    d6, 1
)  # this takes a callable and a sentinel (stop value) and returns a callable iterator
print(i)  # this is a callable iterator object
for roll in i:  # stop when we hit the 1
    print(roll)

print(list(i))  # now returns nothign as the uselss and exhausted :)
