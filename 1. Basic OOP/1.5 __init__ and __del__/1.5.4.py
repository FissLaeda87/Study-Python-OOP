import random
import time

class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

ts = time.time()
elements = []
for i in range(217):
    obj = random.randint(1, 3)
    a, b, c, d = (random.randint(-100, 100) for _ in range(4))
    match obj:
        case 1:
            elements.append(Line(a, b, c, d))
        case 2:
            elements.append(Ellipse(a, b, c, d))
        case 3:
            elements.append(Rect(a, b, c, d))

te = time.time()
dt = te - ts
print(f"Время создания объектов - {dt}")
print(len(elements))


ts = time.time()
for obj in elements:
    if isinstance(obj, Line):
        obj.ep = (0, 0)
        obj.sp = (0, 0)

te = time.time()
dt = te - ts
print(f"Время обнуления объектов - {dt}")
print(elements[2].sp)