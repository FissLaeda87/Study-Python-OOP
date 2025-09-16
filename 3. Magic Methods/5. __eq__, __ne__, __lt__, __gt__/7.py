class FileAcceptor:
    def __init__(self, *args):
        self._extentions = list(map(lambda x: x.strip('!?,. ').lower(), args))

    def __call__(self, filename: str, *args, **kwargs):
        return filename.strip('!?, ').lower().split('.')[-1] in self._extentions

    def __add__(self, other):
        return FileAcceptor(*(self._extentions + other._extentions))


filenames = ["boat.jpg", "ans.web.png", "text.txt", "eq.xls"]
ac1 = FileAcceptor("jpg", "jpeg", "png")
ac2 = FileAcceptor("txt", "doc")
ac12 = ac1 + ac2
print(ac12._extentions)
filenames = list(filter(ac1 + ac2, filenames))
print(filenames)


