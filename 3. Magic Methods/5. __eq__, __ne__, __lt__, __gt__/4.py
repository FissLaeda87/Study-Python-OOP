class Dimensions:
    MIN_DIMENSION = 1
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION and type(value) in (int, float):
            object.__setattr__(self, key, value)
        else:
            raise ValueError("Выходит за диапазон")

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value

    def __le__(self, other):
        return self.a * self.b * self.c <= other.a * other.b * other.c

    def __lt__(self, other):
        return self.a * self.b * self.c < other.a * other.b * other.c


class ShopItem:
    def __init__(self, name, price, dim: Dimensions):
        self.name = name
        self.price = price
        self.dim = dim


dim1 = Dimensions(2, 2, 2)
dim2 = Dimensions(4, 2, 1)
print(dim1 > dim2)

lst_shop = [ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
            ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
            ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)),
            ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))]
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.b * x.dim.a * x.dim.c)
print(*(x.name for x in lst_shop_sorted))

