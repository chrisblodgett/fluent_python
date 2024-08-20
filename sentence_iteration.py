"""
if it implements len and and getitem we can use it as in iterator
    """

import re
import reprlib
from collections.abc import Iterator
from typing import Protocol, TypeVar

RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text) -> None:
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return f'Sentence{reprlib.repr(self.text)}'


print('-----------------')
print('Sentence iteration')

s = Sentence("'The time has come', the Walrus said")
print(s.__repr__())  # repr abbreviates it to 30 chars or less and adds ...
for word in s:  # the instance is an iterable
    print(word)
print(list(s))
print(iter(s))


class SentenceIterable(Iterator):
    def __init__(self, text) -> None:
        self.text = text
        self.words = RE_WORD.findall(text)

    def __iter__(self):
        for word in self.words:
            yield word  # returns iterable

    def __next__(self):
        pass

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return f'Sentence{reprlib.repr(self.text)}'


s2 = SentenceIterable("'The time has come', the Walrus said")
print(list(s2))


class SentenceIterableYield:
    def __init__(self, text) -> None:
        self.text = text

    def __iter__(self):
        return (
            match.group() for match in RE_WORD.finditer(self.text)
        )  # generator expression with ()


s3 = SentenceIterableYield("'The time has come', the Walrus said")
print(list(s2))
