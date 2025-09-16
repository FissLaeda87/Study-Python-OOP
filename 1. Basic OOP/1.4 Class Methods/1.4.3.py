import sys

class StreamData:
    def create(self, fields: tuple[str], lst_values: list[str]) -> bool:
        if len(lst_values) == len(fields):
            [setattr(self, fields[i], lst_values[i]) for i in range(len(fields))]
            return all([hasattr(self, at) for at in fields])
        else:
            return False


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()