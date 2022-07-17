def decorator(func):
    name = f'{func.__qualname__}'.split('.')
    
    def doc(self):
        file = open(name[0], 'w')
        file.write(f'{func(self)}')
        file.close()
        return func(self)
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
