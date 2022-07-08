def simple_number(b):
    a = 0
    while a < b:
        a += 1
        if a % 2 != 0:
            yield a
    return


x = simple_number(100)
for i in x:
    print(i)
