class Book:
    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in ('title', 'author'):
            if not isinstance(value, str):
                raise TypeError("Неверный формат данных")
            else:
                object.__setattr__(self, key, value)
        elif key in ('pages', 'year'):
            if not isinstance(value, int):
                raise TypeError("Неверный формат данных")
            else:
                object.__setattr__(self, key, value)


book = Book("Введение в Питон", "С.А. Балакирев", 500, 2025)
print(book.__dict__)