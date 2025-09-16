class Translator:
    def add(self, eng: str, rus: str) -> None:
        if not hasattr(self, 'data'):
            self.data: dict[list[str]] = dict()
        if eng in self.data:
            if rus in self.data[eng]:
                pass
            else:
                self.data[eng].append(rus)
        else:
            self.data[eng] = [rus]

    def remove(self, eng):
        if eng in self.data:
            del self.data[eng]

    def translate(self, eng) -> list:
        if eng in self.data:
            return self.data[eng]

tr = Translator()
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('go', 'идти')
print(tr.translate('car'))
print(tr.translate('go'))
tr.remove('car')
print(tr.translate('car'))