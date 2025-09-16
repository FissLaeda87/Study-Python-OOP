class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = cls

class MoneyR:
    def __init__(self, money = 0):
        self.volume = money
        self.cb: CentralBank = None

    @property
    def volume(self):
        return self.__volume
    @volume.setter
    def volume(self, n):
        self.__volume = n

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, n):
        self.__cb = n

    def equiv(self):
        return round(self.volume, 1)

    def __eq__(self, other):
        return self.equiv() == other.equiv()

    def __lt__(self, other):
        return self.equiv() < other.equiv()

    def __le__(self, other):
        return self.equiv() <= other.equiv()


class MoneyD:
    def __init__(self, money=0):
        self.volume = money
        self.cb: CentralBank = None

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, n):
        self.__volume = n

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, n):
        self.__cb = n

    def equiv(self):
        return round(self.volume * self.cb.rates['rub'], 1)

    def __eq__(self, other):
        return self.equiv() == other.equiv()

    def __lt__(self, other):
        return self.equiv() < other.equiv()

    def __le__(self, other):
        return self.equiv() <= other.equiv()


class MoneyE:
    def __init__(self, money=0):
        self.volume = money
        self.cb: CentralBank = None

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, n):
        self.__volume = n

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, n):
        self.__cb = n

    def equiv(self):
        return round(self.volume * self.cb.rates['rub'] * self.cb.rates['euro'], 1)

    def __eq__(self, other):
        return self.equiv() == other.equiv()

    def __lt__(self, other):
        return self.equiv() < other.equiv()

    def __le__(self, other):
        return self.equiv() <= other.equiv()

r = MoneyR(45000)
d = MoneyD(500)
CentralBank.register(r)
CentralBank.register(d)
if r > d:
    print('GOOD!')
else:
    print('Not Good:(')