import time

class Point:

    def __init__(self, x: int, y: int, color: str = 'black'):
        self.x = x
        self.y = y
        self.color = color


ts = time.time()
points = [Point(i * 2 + 1, i * 2 + 1, 'yellow') if i == 1 else Point(i * 2 + 1, i * 2 + 1) for i in range(1000)]
te = time.time()
dt = te - ts
print(f"Время создания 1000 объектов = {dt}")
print(points[999])