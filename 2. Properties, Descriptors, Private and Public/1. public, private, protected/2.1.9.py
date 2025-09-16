class ObjList:
    def __init__(self, s: str):
        self.__data = s
        self.__next = None
        self.__prev = None

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, s):
        self.__data = s

    def get_data(self):
        return self.__data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj: ObjList):
        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            obj.set_prev(self.tail)
            self.tail.set_next(obj)
            self.tail = obj


    def remove_obj(self):
        if self.tail == self.head:
            return
        else:
            self.tail.get_prev().set_next(None)
            self.tail = self.tail.get_prev()


    def get_data(self):
        data = []
        obj = self.head
        while obj:
            data.append(obj.get_data())
            obj = obj.get_next()
        return data





lst = LinkedList()
lst.add_obj(ObjList("Данные 1"))
lst.add_obj(ObjList("Данные 2"))
lst.add_obj(ObjList("Данные 3"))
print(lst.get_data())