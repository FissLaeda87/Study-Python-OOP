class StackObj:
    def __init__(self, s):
        self.__data = None
        self.__next = None
        self.data = s
        self.__data = self.data



    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if type(obj) == StackObj or obj is None:
            self.__next = obj

class Stack:
    def __init__(self):
        self.top = None
        self.tail = None

    def push(self, obj: StackObj):
        if self.top is None:
            self.top = obj
            self.tail = obj
        else:
            self.tail.next = obj
            self.tail = obj

    def pop(self):
        if self.top is None:
            return
        if self.top == self.tail:
            del self.top
        else:
            obj: StackObj = self.top
            while obj.next.next is not None:
                obj = obj.next
            obj.next = None

    def get_data(self):
        obj: StackObj = self.top
        data = []
        while obj:
            data.append(obj.data)
            obj = obj.next
        return data

st = Stack()
[st.push(StackObj(f"Объект {i}")) for i in range(5)]
print(st.get_data())
print(st.pop())
print(st.get_data())

