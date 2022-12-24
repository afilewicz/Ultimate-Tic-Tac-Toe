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
