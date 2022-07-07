class Product:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'


class Back:

    def __init__(self, name):
        self.name = name
        self.list = []

    def __iadd__(self, other):
        if isinstance(other, Product):
            self.list.append(other)
        return self

    def __iter__(self):
        return BackIter(self.list)


class BackIter:

    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index += 1
            return self.wrapped[self.index - 1]
        raise StopIteration
    
    def __iter__(self):
        return self


apple = Product('apple')
banana = Product('banana')
tomato = Product('tomato')
back = Back('Aleksandr')
back += apple
back += banana
back += tomato

for product in back:
    print(product)