class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def __setattr__(self, key, value):
        if type(value) not in (float, int):
            raise TypeError("Неизвестный тип присваиваемых данных")
        if key == 'radius' and value <= 0:
            return
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False


    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value


circle = Circle(10.5, 7, 22)
circle.radius = -10
print(circle.__dict__)
x, y = circle.x, circle.y
res = circle.name
print(res)