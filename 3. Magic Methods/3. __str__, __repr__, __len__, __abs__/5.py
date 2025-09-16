class ObjList:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

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

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

class LinkedList:
    def __init__(self):
        self.head: ObjList = None
        self.tail: ObjList = None

    def add_obj(self, obj: ObjList):
        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj

    def remove_obj_indx(self, indx):
        obj = self.head
        for i in range(indx):
            obj = obj.next
        if obj != self.tail:
            obj.prev.next = obj.next
            obj.next.prev = obj.prev
        else:
            self.tail = obj.prev
            self.tail.next = None
        return obj

    def __len__(self):
        n = 1
        obj = self.head
        while obj != self.tail:
            n += 1
            obj = obj.next
        return n

    def linked_lst(self, indx):
        obj = self.head
        for i in range(indx):
            obj = obj.next
        return obj.data

ll = LinkedList()
ll.add_obj(ObjList('1'))
ll.add_obj(ObjList('2'))
ll.add_obj(ObjList('3'))
ll.add_obj(ObjList('4'))
ll.add_obj(ObjList('5'))
print(len(ll))
print(ll.linked_lst(2))
print(ll.remove_obj_indx(4))
print(len(ll))
print(ll.linked_lst(3))
