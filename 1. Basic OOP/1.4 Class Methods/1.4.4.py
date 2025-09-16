import sys

# программу не менять, только добавить два метода
#lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a, b) -> list[dict]:
        b = len(self.lst_data) if b >= len(self.lst_data) else b
        return self.lst_data[a:b]

    def insert(self, data: list[str]) -> None:
        self.lst_data.append([{self.FIELDS[i]: row.split()[i] for i in range(len(self.FIELDS))} for row in data])

lst_in = [
    "1 Сургуй 35 12000", "2 Федор 23 120000", "3 Иван 13 1200"
]

db = DataBase()
db2 = DataBase()
db.insert(lst_in)
print(db.select(0, 5))
print(db2.select(0, 8)) #Получается, так как список - изменяемый тип, который передается
                            # по ссылке, то все экземкляры объектов класса добавляют и используют один и тот же список класса