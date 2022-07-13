def fibonachi():
    first = 0
    second = 1
    alist = []

    def next(i: int):
        nonlocal first
        nonlocal second
        while len(alist) < i:
            new = second + first
            first = second
            second = next
            alist.append(new)
            return alist

    return next


f = fibonachi()
for i in f(20):
    print(i)
