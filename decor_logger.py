import time


def log(funk):

    def decor(*args):

        def loger(n, file):
            f = open(file, 'w')
            start_time = time.time()

            for _ in range(n):
                funk(*args)
                f.write(f'\n{time.time() - start_time}')
            f.close()
            return funk(*args)

        return loger

    return decor


@log
def suma(a, b):
    return a + b


print(suma(2, 4)(5, 'log'))
