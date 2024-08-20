import typing  # this is required for iter()
from functools import partial

with open('./ming.jpeg', 'rb') as f:
    read64 = partial(f.read, 64)  # because we can't pass params in iter we use partial
    # to fix params in place and call with read64
    sizes = [len(s) for s in iter(read64, b'')]
    print(sum(sizes))
