class Point():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y

class Rectangle:
    def __init__(self, x1, y1, x2 = None, y2 = None):
        if x2 is None and y2 is None:
            self.__sp = x1
            self.__ep = y2
        else:
            self.__sp = Point(x1, y1)
            self.__ep = Point(x2, y2)

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f"Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}")

r = Rectangle(0, 0, 20, 34)
r.draw()