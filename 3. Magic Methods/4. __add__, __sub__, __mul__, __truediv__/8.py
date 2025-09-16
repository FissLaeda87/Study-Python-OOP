class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        return self.money + other.money

    def __radd__(self, other):
        return self.money + other

class Budget:
    def __init__(self):
        self.data = []

    def add_item(self, it: Item):
        self.data.append(it)

    def remove_item(self, indx):
        del self.data[indx]

    def get_items(self):
        return self.data

b = Budget()
b.add_item(Item("Курс 1", 1000))
b.add_item(Item("Курс 2", 2000))
b.add_item(Item("Курс 3", 3000))
b.add_item(Item("Курс 4", 4000))
b.add_item(Item("Курс 5", 5000))
print(b.get_items())
b.remove_item(2)
print(b.get_items())
s = 0
for x in b.get_items():
    s = s + x

print(s)
