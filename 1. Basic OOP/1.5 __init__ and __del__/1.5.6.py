class Graph:
    def __init__(self, data: list[int]):
        self.data = data.copy()
        self.is_show = True

    def set_data(self, data: list[int]):
        self.data = data.copy()

    def set_show(self, fl_show: bool):
        self.is_show = fl_show

    def close(self):
        print("Отображение данных закрыто")

    def show_table(self):
        if self.is_show:
            print(*self.data)
        else:
            self.close()

    def show_graph(self):
        if self.is_show:
            print(f"Графическое отображение данных: {' '.join(list(map(str, self.data)))}")
        else:
            self.close()

    def show_bar(self):
        if self.is_show:
            print(f"Столбчатая диаграмма: {' '.join(list(map(str, self.data)))}")
        else:
            self.close()

# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, input().split()))

gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()