def square(start, n):
    return [i ** 2 for i in range(start, n)]


def square_root(start, n):
    return [i ** 0.5 for i in range(start, n)]


def generator_func(func, start, n):
    try:
        for i in func(start, n):
            yield i
    except GeneratorExit:
        pass


a = generator_func(square, 2, 10)
b = generator_func(square_root, 27, 100)

for i in a:
    if i == 25:
        a.close()
    print(i)
