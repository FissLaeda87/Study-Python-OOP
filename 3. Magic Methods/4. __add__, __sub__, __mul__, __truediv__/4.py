class NewList:
    def __init__(self, data: list = None):
        if data is None:
            self.data = []
        else:
            self.data = data

    def get_list(self):
        return self.data

    def __sub__(self, other):
        return NewList([item for item in self.data if item not in other.data])

    def __rsub__(self, other):
        return NewList([item for item in other.data if item not in self.data])

    def __isub__(self, other):
        self.data = [item for item in self.data if item not in other.data]

lst1 = NewList([1,2,3,4,5,6,7,8,9,10])
lst2 = NewList([8, 9, 10, 11, 12])
res = lst1 - lst2
print(res.get_list())
