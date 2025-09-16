class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, p):
        self.goods.append(p)

    def remove_product(self, p):
        self.goods.remove(p)


class StringValue:
    def __init__(self, max = 50, min = 2):
        self.max_length = max
        self.min_length = min

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if self.min_length <= len(value) <= self.max_length:
            instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]



class PriceValue:
    def __init__(self, max = 10000):
        self.max_value = max


    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if 0 <= value <= self.max_value:
            instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price


shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Пайтону", 0))
shop.add_product(Product("Курс по Пайтон ООП", 5000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")
