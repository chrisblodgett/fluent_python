"""
This sample class demonstrates how to add pythonic functionality to user defined classes

"""

import functools
import math
import operator
import reprlib
from array import array
from typing import Any


class Vector:
    typecode = 'd'  # default type code, 8 byte double precision float
    __match_args__ = ('x', 'y', 'z', 't')

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __len__(self):
        return len(self._components)

    def __hash__(self):
        hashes = (hash(x) for x in self._components)  # we could use map here instead
        # hashes = map(hash, self._components) # works the same way
        return functools.reduce(operator.xor, hashes, 0)

    def __eq__(self, other):
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __getitem__(self, index):
        # if we get a slice then return a new vector
        if isinstance(index, slice):
            cls = type(self)
            return cls(self._components[index])
        index = operator.index(index)  # get an index form the key
        return self._components[index]

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[
            components.find('[') : -1
        ]  # remove the prefix 'd' and the trailing
        return f'Vector({components})'

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(
            array(self.typecode, self._components)
        )  # we use the class attribute typecode to provide a default value

    def __abs__(self):
        return math.hypot(*self)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = octets[0]
        memv = memoryview(octets[1:]).cast(typecode)
        # memory view from octets binary seq and typecode to cast
        return cls(memv)  # unpack it and return it to teh class constructor

    def __getattr__(self, name):  # called when attribute lookup fails
        cls = type(self)
        try:
            pos = cls.__match_args__.index(
                name
            )  # try to match the name with the match args list
        except ValueError:
            pos = -1

        if 0 <= pos < len(self._components):
            return self._components[pos]  # return the value for the x,y,z...
        msg = f'{cls.__name__!r} object has no attribute {name!r}'
        raise AttributeError(msg)

    def __setattr__(self, name: str, value: Any, /) -> None:
        # ` don't allow assigning single character attributes because of conflicts with built in x,y,z used in __getattr__
        cls = type(self)
        if len(name) == 1:
            if name in cls.__match_args__:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ""
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(
            name, value
        )  # default to the super() class setattr behaivor


v1 = Vector([3, 4, 5])
print(len(v1))
print(v1[0])
print(v1.y)
