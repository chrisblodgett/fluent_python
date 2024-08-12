import functools

from clockdeco_param import clock


@clock()
def fibonacci_slow(n):
    if n < 2:
        return n
    return fibonacci_slow(n - 2) + fibonacci_slow(n - 1)


@functools.cache  # this will make it go fast because it won't execute functions it already has done over again
@clock()
def fibonacci_fast(n):
    if n < 2:
        return n
    return fibonacci_fast(n - 2) + fibonacci_fast(n - 1)


print(fibonacci_fast(30))
