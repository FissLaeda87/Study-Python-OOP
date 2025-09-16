class ListMath:
    def __init__(self, data: list = None):
        if not data:
            self.data = []
        else:
            self.data = [i for i in data if type(i) in (int, float)]

    @staticmethod
    def operation(data: list, numb: int, char):
        if char == '+':
            return [i + numb for i in data]
        elif char == '-':
            return [i - numb for i in data]
        elif char == '*':
            return [i * numb for i in data]
        elif char == '/':
            return [i / numb for i in data]

    def __add__(self, other):
        return ListMath(self.operation(self.data, other, '+'))
    def __radd__(self, other):
        return ListMath(self.operation(self.data, other, '+'))
    def __iadd__(self, other):
        self.data = self.operation(self.data, other, '+')

    def __sub__(self, other):
        return ListMath(self.operation(self.data, other, '-'))
    def __rsub__(self, other):
        return ListMath([self.operation([other], item,'-') for item in self.data])
    def __isub__(self, other):
        self.data = self.operation(self.data, other, '-')

    def __mul__(self, other):
        return ListMath(self.operation(self.data, other, '*'))
    def __mul__(self, other):
        return ListMath(self.operation(self.data, other, '*'))
    def __mul__(self, other):
        self.data = self.operation(self.data, other, '*')

    def __truediv__(self, other):
        return ListMath(self.operation(self.data, other, '/'))

    def __truediv__(self, other):
        return ListMath([self.operation([other], item, '/') for item in self.data])

    def __truediv__(self, other):
        self.data = self.operation(self.data, other, '/')
