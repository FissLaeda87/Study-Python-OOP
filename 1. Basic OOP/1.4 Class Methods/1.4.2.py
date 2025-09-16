class Graph:
    LIMIT_Y: list[int] = [0, 10]
    def set_data(self, data: list[int]) -> None:
        self.data: list[int] = data

    def draw(self):
        print(*[x for x in self.data if self.LIMIT_Y[0] <= x <= self.LIMIT_Y[1]])

graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()

