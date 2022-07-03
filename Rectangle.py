class Rectangle:

    def __init__(self, width: int | float, height: int | float):
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

    def __gt__(self, other):
        return self.square() > other.square()
    #
    # def __ge__(self, other):
    #     return self.square() >= other.square()

    def __lt__(self, other):
        return self.square() < other.square()
    #
    # def __le__(self, other):
    #     return self.square() <= other.square()
    #
    # def __eq__(self, other): Вы сказали что сравнивать float не хорошо так что не знаю правильно ли я сделал
    #     return self.square() == other.square()
    #
    # def __neq__(self, other):
    #     return self.square() != other.square()

    def __add__(self, other):
        return self.square() + other.square()

    def __mul__(self, other):
        return self.square() * other

    def __str__(self):
        return f'Width = {self.width}\nHeight = {self.height}\nS = {self.square()}\n'


rect_1 = Rectangle(10, 15)
rect_2 = Rectangle(5, 10)
rect_3 = Rectangle(20, 30)
print(rect_1)
print(rect_2 < rect_3)

