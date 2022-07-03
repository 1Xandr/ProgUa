class Product:

    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} = {self.price}'


class Buyer:

    def __init__(self, name: str, index: str):
        self.name = name
        self.index = index

    def __str__(self):
        return f'{self.name}\n{self.index}'


class Order:

    def __init__(self, buyer: Buyer):
        self.buyer = buyer
        self.cart = []
        self.kol = []

    def __iadd__(self, other, que):
        if isinstance(other, Product):
            self.cart.append(other)
            self.kol.append(que)
        return self

    def total_price(self):
        total = 0
        for i, item in enumerate(self.cart):
            total += item.price * self.kol[i]
        return total

    def __str__(self):
        res = f'{self.buyer}'

        for i, item in enumerate(self.cart):
            tmp = f'\n{item} UAH X {self.kol[i]} = {self.kol[i] * item.price}'
            res += tmp

        res += f'\n{self.total_price()} UAH'
        return res


apple = Product('apple', 5)
banana = Product('banana', 10)
buyer_1 = Buyer('Alex', '123')
buyer_2 = Buyer('Andrey', '456')
order = Order(buyer_1)
order += apple, 1 # Не рабоатет
order.__iadd__(apple, 1) # Работает 
order.__iadd__(banana, 2)
print(order)
