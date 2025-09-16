class FloatValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise TypeError("Присваивать можно только вещественный тип данных.")
        else:
            setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, v = 0.0):
        self.value = v

class TableSheet:
    def __init__(self, N, M):
        self.cells: list[list[Cell]] = []
        i = 1.0
        for _ in range(N):
            l = []
            for a in range(M):
                l.append(Cell(i))
                i += 1.0
            self.cells.append(l)

table = TableSheet(5, 3)
print(table.cells)
