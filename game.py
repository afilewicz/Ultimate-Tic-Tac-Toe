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
        self.winned_square = []

    @property
    def player(self):
        return self._player

    @property
    def computer(self):
        return self._computer

    @property
    def result(self):
        return self._result

    def checking_if_win_square(self, square, person):
        column_0 = column_1 = column_2 = 0
        row_0 = row_1 = row_2 = 0
        diagonal_1 = diagonal_2 = 0
        for i, field in enumerate(self.board.areas[square]):
            if field == person.sign:
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
                    diagonal_1 += 1
                if i % 4 == 2 or i == 4:
                    diagonal_2 += 1
        any_3 = [column_0, column_1, column_2, row_0, row_1, row_2, diagonal_1, diagonal_2]
        if 3 in any_3:
            return True

    def win(self, person):
        winned_squares = []
        if person == self.player:
            winned_squares = self.board.winned_squares_player
        else:
            winned_squares = self.board.winned_squares_computer
        column_0 = column_1 = column_2 = 0
        row_0 = row_1 = row_2 = 0
        diagonal_1 = diagonal_2 = 0
        for i, field in enumerate(self.board.areas):
            if i in winned_squares:
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
                    diagonal_1 += 1
                if i % 4 == 2 or i == 4:
                    diagonal_2 += 1
        any_3 = [column_0, column_1, column_2, row_0, row_1, row_2, diagonal_1, diagonal_2]
        if 3 in any_3 and person == self.player:
            self._result = True
        if 3 in any_3 and person == self.computer:
            self._result = False

    def round(self):
        self.board.make_board()
        square = self.player.move(self)
        if self.checking_if_win_square(square, self.player):
            self.board.winned_squares_player.append(square)
            self.win(self.player)
        square_com = self.computer.move(self)
        if self.checking_if_win_square(square_com, self.computer):
            self.board.winned_squares_computer.append(square_com)
            self.win(self.computer)
