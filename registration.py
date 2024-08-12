registry = []


def register(func):
    """a function to register a function"""
    print(f"registering function {func}")
    registry.append(func)  # append the function to the registery
    return func


@register
def func1():
    print('calling func1')


if __name__ == '__main__':
    func1()
    func1()
