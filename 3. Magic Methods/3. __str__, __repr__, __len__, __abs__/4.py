class WordString:
    def __init__(self, string: str = ""):
        self.__string = string

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value):
        self.__string = value

    def __len__(self):
        return len(self.string.split())

    def words(self, indx: int):
        return self.__string.split()[indx]

words = WordString()
words.string = "Курс по   Питону номер  1"
print(len(words))
print(words.words(2))