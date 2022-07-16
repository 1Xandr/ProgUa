list_decotators = []


def decorators(func):
    def read(a):
        list_decotators.append(func)
        return func(a)
    return read


@decorators
def plus(a):
    return a + 1

@decorators
def minus(a):
    return a - 1


print(list_decotators)
print(plus(10))
print(minus(10))
print(list_decotators)
