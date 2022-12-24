from board import Board
from player import Player
from computer import Computer


class Game:
    def __init__(self, player: Player, computer: Computer, board=Board()):
        self._player = player
        self._computer = computer
        self._result = None
        self.board = board
        if self.player.sign == 'X':
            self.computer.sign == 'O'
        else:
            self.computer.sign == 'X'

    @property
    def player(self):
        return self._player

    @property
    def computer(self):
        return self._computer

    @property
    def result(self):
        return self._result

    def round(self, x, y):
        board = self.board
        board.make_board()
        column, row = self.player.move(x, y)
        self.board.set(column, row, self.player.sign)
        com_column, com_row = self.computer.move()
        self.board.set(com_column, com_row, self.computer.sign)

    def winning_square(self, new, sign):
        column_0 = column_1 = column_2 = 0
        row_0 = row_1 = row_2 = 0
        diagonal_1 = diagonal_2 = 0
        square = new[0]
        for i in range(9):
            if self.board.areas[square][i] == sign:
                if i % 3 == 0:
                    column_0 += 1
                elif i % 3 == 1:
                    column_1 += 1
                elif i % 3 == 2:
                    column_2 += 1
                if i//3 == 0:
                    row_0 += 1
                elif i//3 == 1:
                    row_1 += 1
                elif i//3 == 2:
                    row_2 += 1
                if i % 4 == 0:
                    diagonal_1 += 0
                if i % 4 == 2 or i == 4:
                    diagonal_2 += 0
