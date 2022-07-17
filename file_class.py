def decorator(func):

    def doc(self):
        file = open(Product.__name__, 'w')
        file.write(f'{func}')
        file.close()
        return file
    return doc


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @decorator
    def __str__(self):
        return f'Name = {self.name}\nPrice = {self.price}'


apple = Product('apple', 5)
print(apple)
