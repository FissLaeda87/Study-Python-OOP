class Telecast:
    def __init__(self, id, name, duration):
        self.uid = id
        self.name = name
        self.duration = duration

    @property
    def uid(self):
        return  self.__id

    @uid.setter
    def uid(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration

class TVProgram:
    def __init__(self, s):
        self.name = s
        self.items: list[Telecast] = []

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        for t in self.items:
            if t.uid == indx:
                self.items.remove(t)

Telecast(1, 'ASDFG', 100)