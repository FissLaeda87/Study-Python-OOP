class Descriptor:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __set__(self, instance, value):
        instance.__dict__[self.name]= value

    def __get__(self, instance, owner):
        getattr(instance, self.name)




class Dimensions:
    MIN_DIMENSION = 0
    MAX_DIMENSION = 1000
    a = Descriptor()
    b = Descriptor()
    c = Descriptor()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять эти атрибуты запрещено")
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            object.__setattr__(self, key, value)

d = Dimensions(10, 20, 30)
print(d.__dict__)
d.a = 8
d.b = 15
print(d.__dict__)
d.__a = 100
print(d.__a)
