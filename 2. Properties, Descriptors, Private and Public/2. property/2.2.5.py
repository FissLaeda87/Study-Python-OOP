class WindowDlg:
    def __init__(self, title, width, heigth):
        self.__title = title
        self.__width = width
        self.__heigth = heigth

    @staticmethod
    def check_size(size):
        return isinstance(size, int) and 0 <= size <= 1000

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__heigth}")

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        if self.check_size(width):
            self.__width = width
            self.show()

    @property
    def heigth(self):
        return self.__heigth

    @heigth.setter
    def heigth(self, heigth):
        if self.check_size(heigth):
            self.__heigth = heigth
            self.show()

w = WindowDlg("Lbfkju 1", 300, 200)
w.width = 500
w.heigth = 700
w.width = 5.6