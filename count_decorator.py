def decorator(func):
    count = 0

    def count_times(yname):
        nonlocal count
        count += 1
        return f'Your name is {func(yname)}', count

    return count_times


@decorator
def name(yname):
    return f'Your name is {yname}'


print(name('Aleksandr'))
print(name('Aleksandr'))
