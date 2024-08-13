"""
This sample class demonstrates how to add pythonic functionality to user defined classes

    """

import math
from array import array


class Vector2d:
    typecode = 'd'

    __match_args__ = (
        'x',
        'y',
    )  # this so we define the order of are attributes for class attribute pattern

    # matching
    @classmethod
    def frombytes(cls, octets):
        typecode = octets[0]
        memv = memoryview(octets[1:]).cast(typecode)
        # memory view from octets binary seq and typecode to cast
        return cls(*memv)  # unpack it and return it to teh class constructor

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def angle(self):
        return math.atan2(self.__y, self.__x)

    def __hash__(self):
        return hash((self.x, self.y))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))


v1 = Vector2d(1, 0)
v2 = Vector2d(0, 1)
v3 = Vector2d(0, 0)
v4 = Vector2d(1, 1)

print(v1, v2)
print(repr(v1))
print(v1 == [1, 0])
print(format(v1, '.3e'))  # this owkr sbecause we dfined the __format__
print('hash- ', hash(v1))


def keyword_pattern_demo(v: Vector2d) -> None:
    match v:
        case Vector2d(x=0, y=0):
            print(f'{v!r} is null')
        case Vector2d(x=x, y=y) if x == y:
            print(f'{v!r} is diagonol')
        case _:
            print(f'{v!r} is awesome')


def positional_pattern_demo(v: Vector2d) -> None:
    match v:
        case Vector2d(0, 0):
            print(f'{v!r} is null')
        case Vector2d(x, y) if x == y:
            print(f'{v!r} is diagonol')
        case _:
            print(f'{v!r} is awesome')


print(keyword_pattern_demo(v3))
print(keyword_pattern_demo(v4))
