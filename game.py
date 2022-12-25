from board import Board
from player import Player
from computer import Computer


class Game:
    def __init__(self, player: Player, computer: Computer, board=Board()):
        self._player = player
        self._computer = computer
        self._players = [player, computer]
        self._result = None
        self.board = board
        if self.player.sign == 'X':
            self.computer._sign = 'O'
        else:
            self.computer._sign = 'X'

    @property
    def player(self):
        return self._player

    @property
    def computer(self):
        return self._computer

    @property
    def players(self):
        return self._players

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
        any_3 = [
            column_0, column_1, column_2,
            row_0, row_1, row_2,
            diagonal_1, diagonal_2
        ]
        if 3 in any_3:
            return True

    def win(self, person):
        winned_squares = person.winned_squares
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
        any_3 = [
            column_0, column_1, column_2,
            row_0, row_1, row_2,
            diagonal_1, diagonal_2
        ]
        if 3 in any_3 and person == self.player:
            self._result = True
        if 3 in any_3 and person == self.computer:
            self._result = False

    def round(self):
        self.board.draw_board()
        for person in self.players:
            square = person.move(self)
            if self.checking_if_win_square(square, person):
                person.winned_squares.append(square)
                self.win(person)
