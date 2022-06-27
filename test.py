class ErrorTest(Exception):

    def __init__(self, error):
        self.error = error


a = float(input("Введите цену: ")) # Проверку на ввод букв можно делать потому что я уже написал float


def count(x: int):
    if not isinstance(x, float):
        raise ErrorTest('Пожалуйста введите целое число')
    elif x < 0:
        raise ErrorTest('Можно вводить только положительные числа')

    print(f'\nName: Apple\nPrice : {x}')


count(a)


def abstr(x):  # Для обработки отрицательных чисел
    print(list(map(abs, x)))

# kist = [a]
# abstr(kist)
