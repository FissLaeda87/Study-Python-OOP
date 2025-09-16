class StackObject:
    def __init__(self, data):
        self.data = data
        self.next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj: StackObject):
        if not self.top:
            self.top = obj
        else:
            o = self.top
            while o.next:
                o = o.next
            o.next = obj

    def pop_back(self):
        o = self.top
        if not self.top:
            return
        elif not self.top.next:
            self.top = None
            return o
        else:
            while o.next.next:
                o = o.next
            obj = o.next
            o.next = None
            return obj

    def get_data(self):
        obj = self.top
        while obj:
            print(obj.data)
            obj = obj.next


    def __add__(self, other: StackObject):
        self.push_back(other)
        return self

    def __mul__(self, other: list[StackObject]):
        [self.push_back(obj) for obj in other]
        return self

stack = Stack()
stack.push_back(StackObject('1'))
stack = stack + StackObject('2')
stack += StackObject('3')
stack.get_data()
stack = stack * [StackObject('4'), StackObject('5')]
stack.pop_back()
stack.get_data()

