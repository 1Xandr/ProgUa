def math(n: int):
    if n == 0:
        raise ValueError
    number = 1
    while True:
        try:
            first_number = number * n
            number = first_number
            yield number
        except GeneratorExit:
            break


x = math(-2)
print(next(x))
print(next(x))
print(next(x))
