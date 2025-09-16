class Product:
    id = 1
    d = {'name' : (str,), 'weigth' : (float, int), 'price' : (float, int)}
    def __init__(self, name, weigth, price):
        self.id = Product.id
        Product.id += 1
        self.name = name
        self.weigth = weigth
        self.price = price

    def __setattr__(self, key, value):
        if key in self.d:
            if type(value) in self.d[key]:
                super().__setattr__(key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise TypeError("Нельзя удалять id")
        else:
            object.__delattr__(self, item)

class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product: Product):
        self.goods.append(product)

    def remove_product(self, product: Product):
        self.goods.remove(product)

p1 = Product("Nokia", 100, 5000)
p2 = Product('Samsung', 500, 25000)
shop = Shop("Mobile Salon")
print(p1.__dict__)
shop.add_product(p1)
shop.add_product(p2)
shop.remove_product(p2)
print(shop.goods)