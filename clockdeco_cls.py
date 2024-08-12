"""
Another way to do decorators with a __call__ in a class
"""

import time

DEFAULT_FMT = '[{elapsed:0.8F}s] {name}({args}) -> {result}'  # a format string you can use with .format and pass it dictionary of arguments


class clock:  # this is our paramerized decorator factor instead of howaving an outter function

    def __init__(self, fmt=DEFAULT_FMT):
        self.fmt = fmt

    def __call__(self, func):  # make the class instance callable with __call__
        def clocked(*_args):
            t0 = time.perf_counter()
            _result = func(*_args)  # clocked wraps this decorated function
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(self.fmt.format(**locals()))
            return _result  # return the result of the function

        return clocked


def snooze(seconds: float) -> float:
    time.sleep(seconds)
    return seconds


print(snooze.__name__)
clk = clock()(snooze)
print(clk.__name__)
r = clk(1)
print(r)
