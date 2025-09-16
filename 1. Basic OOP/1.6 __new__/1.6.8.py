TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            return super().__new__(DialogWindows)
        else:
            return super().__new__(DialogLinux)

    def __init__(self, name):
        self.name_class = name

dlg = Dialog("DialogWindows1")
print(dlg)