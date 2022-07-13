a = [i for i in range(20)]
b = [i for i in range(20, 41)]


def square(alist):
    return [i ** 2 for i in alist]


def func(function, alist):
    a = [i for i in function(alist)]
    return sum(a)


print(func(square, a))

