import random

class Cell:
    def __init__(self, around_mines: int = 0, mine: bool = False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True

class GamePole:
    def __init__(self, N, M):
        self.pole = [[Cell() for n in range(N)] for _ in range(N)]
        self.N = N
        self.M = M
        self.init()


    def init(self):
        m = 0
        while m < self.M:
            a = random.randint(0, self.N - 1)
            b = random.randint(0, self.N - 1)
            if self.pole[a][b].mine:
                continue
            else:
                self.pole[a][b].mine = True
                m += 1

        idxs = (-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for i in range(self.N):
            for j in range(self.N):
                count = sum((self.pole[i+x][j+y].mine for x, y in idxs if 0 <= i+x < self.N and 0 <= j+y < self.N))
                self.pole[i][j].around_mines = count

    def show(self):
        for i in range(self.N):
            print(*['#' if self.pole[i][j].fl_open == False else '*' if self.pole[i][j].mine else str(self.pole[i][j].around_mines) for j in range(self.N)])

pole = GamePole(10, 12)
pole.show()