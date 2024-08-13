""" a module to demonstrate function registration using decorators """

registry = set()


def register(active=True):
    print('in register', active)

    def decorate(func):
        print('in decorate ', active)

        def wrapper(*args, **kwargs):
            """a function to register a function"""
            print('in wrapper', active)
            func(args, *kwargs)
            if active:
                print(f"registering function {func}")
                registry.add(func)  # append the function to the registery
            else:
                print('removing fucntion ')
                registry.remove(func)

        return wrapper  # since this is a decorator it must return a function

    return decorate


def register_old(func):
    print(f"registering function {func}")
    registry.add(func)
    return func


@register()
def func1(a: int = 0):
    print('in func1', a)


def func2(a: int = 0):
    print('in func2', a)


if __name__ == '__main__':
    print('calling func1')
    func1(1)
    print('registry: ', registry)
    #    register(False)(func1)
