def new_range(start=0, stop=-1, step=1):
    if start < 0:
        raise ValueError
    if stop < start:
        raise ValueError
    i = 0
    i += start
    while i < stop:
        i += 1
        yield i - 1
    return


x = new_range(3, 10)
for i in x:
    print(i)
