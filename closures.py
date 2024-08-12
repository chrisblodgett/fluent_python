# Closures are functions that retain the bindings of the free variables that exist when the function is defined,


def make_averager():
    """This function returns a closure"""
    series = []  # this is a free variable because it is part of the closure

    def averager(new_val):
        series.append(new_val)
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averager()  # make averager returns a function that is a closure
avg2 = make_averager()  # this will have it's own series list
print(f'average1 is {avg(1)}')
print(f'avarege1 is  {avg(2)}')  # now 1 and 2 are in the series list
print(avg2(100))  # this starts a new series list
print(avg(2))
print(avg2(50))
print(
    avg.__code__.co_freevars, avg.__closure__[0].cell_contents
)  # ('new_val', 'total')
