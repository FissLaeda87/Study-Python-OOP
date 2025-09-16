class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        obj = super().__new__(Point)
        obj.x = self.x
        obj.y = self.y
        return obj

pt = Point(10, 20)
pt_clone = pt.clone()
print(pt, pt_clone)
