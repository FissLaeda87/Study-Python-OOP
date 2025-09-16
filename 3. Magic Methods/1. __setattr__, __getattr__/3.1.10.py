import time


class Mechanical:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and value is not None:
            return
        object.__setattr__(self, key, value)

class Aragon:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and value is not None:
            return
        object.__setattr__(self, key, value)

class Calcium:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and value is not None:
            return
        object.__setattr__(self, key, value)

class GeyserClassic:
    MAX_DATE_FILTER = 100
    def __init__(self):
        self.slots = {1 : None, 2: None, 3: None}

    def add_filter(self, slot, filter):
        d = {1: Mechanical, 2: Aragon, 3: Calcium}
        if d[slot] == type(filter):
            self.slots[slot] = filter

    def remove_filter(self, slot):
        if slot in self.slots:
            self.slots[slot] = None

    def get_filters(self):
        return tuple(self.slots.values())

    def water_on(self):
        slots = set(filter(lambda x: x[1] is not None and (0 <= time.time() - x[1].date <= self.MAX_DATE_FILTER), self.slots))
        return slots == set(self.slots)




