def new_range(start=0, stop=-1, step=1):
    if start < 0:
        raise ValueError
    if stop < start:
        raise ValueError

    index = 0
    alist = []

    while index < stop:
        alist.append(index)
        index += 1

    for a in alist[start:stop:step]:
        yield int(a)
    return


x = new_range(3, 10)
for i in x:
    print(i)
