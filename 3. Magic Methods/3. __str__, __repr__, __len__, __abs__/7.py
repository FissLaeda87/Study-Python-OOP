import math


class RadiusVector:
    def __init__(self, *args):
        self.coords = list(args)


    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, value):
        if  len(value) == 1:
            self.__coords = [0 for _ in range(value[0])]
        elif type(value) in (tuple[int], tuple[float]):
            self.__coords = list(value)
        else:
            return

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        return math.sqrt(sum(cord**2 for cord in self.coords))

    def get_coords(self):
        return tuple(self.coords)

    def set_coords(self, *args):
        if len(args) <= self.__len__():
            self.__coords[0:len(args)] = list(args)
        else:
            self.__coords = list(args[0:self.__len__()])

vec = RadiusVector(3)
print(vec.get_coords())
vec.set_coords(3, -5.6, 8)
print(vec.get_coords())
vec.set_coords(1,2)
print(vec.get_coords())
vec.set_coords(5,4,3,2,1)
print(vec.get_coords())
print(len(vec))
print(abs(vec))

