import time

DEFAULT_FMT = '[{elapsed:0.8F}s] {name}({args}) -> {result}'  # a format string you can use with .format and pass it dictionary of arguments


def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*_args):
            t0 = time.perf_counter()
            _result = func(*_args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result

        return clocked

    return decorate


if __name__ == '__main__':

    @clock()
    def snooze(seconds: float):
        time.sleep(seconds)

    for i in range(3):
        snooze(2)
