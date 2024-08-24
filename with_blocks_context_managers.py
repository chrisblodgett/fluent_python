import contextlib
import sys


class LookingGlass:
    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'  # just so we have something to print on here

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('dont divide by zero')


with LookingGlass() as lg:
    print('ming')
print('ming')

manager = LookingGlass()
monster = manager.__enter__()
print(monster == 'JABBERWOCKY')
print(monster)
manager.__exit__(None, None, None)
print(monster)


# use a generator to reduce boilerplate code by using a single yield to give the __enter_- return


@contextlib.contextmanager  # contextmanager decorator
def looking_glass2():
    original_write = sys.stdout.write

    def reverse_write(
        text,
    ):  # we can call the original_write becauesa it's in the closure
        original_write(text[::-1])

    sys.stdout.write = reverse_write  # replace the sys write with our new write

    yield 'JABBERWOCKY'  # yield the value bound to target variable this is the as clause of a with
    # the body of the with statement is then executed here and the generator pauses
    sys.stdout.write = original_write


with looking_glass2() as gls2:
    print(gls2)
    print('hi')
print('hi')
