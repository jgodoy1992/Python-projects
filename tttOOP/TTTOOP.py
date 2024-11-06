from random import choice


class Board:
    def __init__(self, n):
        self.n = n
        self._cell_w = 5
        self._board = [
            [j + i*self.n for j in range(1, self.n+1)]for i in range(self.n)]

    def build_board(self):

        # self._board = [[j + i*self.n for j in range(1,self.n+1)]for i in range(self.n)]

        for row in range(self.n):
            print(' | '.join(str(celda).center(self._cell_w)
                  for celda in self._board[row]))
            print('+'*(self._cell_w+3)*self.n)

    def is_victory(self, sign):

        self.sign = sign

        for i in range(self.n):
            if all(self._board[i][j] == self.sign for j in range(self.n)) or all(self._board[j][i] == self.sign for j in range(self.n)):
                return True

        if all(self._board[i][i] == self.sign for i in range(self.n)) or all(self._board[i][self.n-1-i] == self.sign for i in range(self.n)):
            return True

        return False

    def list_of_free_cells(self):
        self.free_cells = []

        for i in range(self.n):
            for j in range(self.n):
                if self._board[i][j] != 'X' and self._board[i][j] != 'O':
                    self.free_cells.append((i, j))

        return self.free_cells

    def draw_move(self):
        self.free_cells = self.list_of_free_cells()

        if self.free_cells:

            self.move = choice(self.free_cells)
            self._board[self.move[0]][self.move[1]] = 'X'
            self.build_board()
            return True

        return False

    def user_move(self):

        while True:

            self.move = int(input('Ingrese casilla: '))

            self.row = (self.move - 1) // self.n
            self.col = (self.move - 1) % self.n

            if self._board[self.row][self.col] == self.move:
                self._board[self.row][self.col] = 'O'
                break
            else:
                print('Casilla ocupada o movimiento invalido')
