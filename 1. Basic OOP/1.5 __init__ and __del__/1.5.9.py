import sys

class ListObject:
    def __init__(self, data: list[str]):
        if len(data) > 1:
            self.data = data[0]
            self.next_obj = ListObject(data[1:])
        else:
            self.data = data[0]
            self.next_obj = None

    def link(self, obj):
        if self.next_obj is None:
            self.next_obj = obj
            obj.next_obj = None
        else:
            obj.next_obj = self.next_obj
            self.next_obj = obj



# считывание списка из входного потока (эту строку не менять)
#lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in в программе не менять

lst_in = ["Первые шаги в ООП", "Как правильно проходить этот курс", "Методы классов"]
head_obj = ListObject(lst_in)
print(head_obj.data)
# здесь создаются объекты классов и вызываются нужные методы