class RadiusVector2D:
    MIN_CORD = -100
    MAX_CORD = 1024

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.__x = self.x
        self.__y = self.y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, i):
        if self.MIN_CORD <= i <= self.MAX_CORD:
            self.__x = i

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, i):
        if self.MIN_CORD <= i <= self.MAX_CORD:
            self.__y = i

    @staticmethod
    def norm2(vector):
        return vector.x**2 + vector.y**2

v = RadiusVector2D(2,3)
print(RadiusVector2D.norm2(v))