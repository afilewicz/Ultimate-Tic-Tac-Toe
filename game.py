from board import Board
from player import Player
from computer import Computer
from random import randint


class Game:
    def __init__(self, player: Player, computer: Computer):
        self.board = Board()
        self._player = player
        self._computer = computer
        self._players = [player, computer]
        self._result = None
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

    def checking_if_win_square(self, person, square):
        if square != self.board.areas:
            fields = [person.sign]
            board = self.board.areas[square]
        else:
            fields = person.winned_squares
            board = self.board.areas
        column_0 = column_1 = column_2 = 0
        row_0 = row_1 = row_2 = 0
        diagonal_1 = diagonal_2 = 0
        for i, field in enumerate(board):
            if field in fields:
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

    def player_move(self):
        while True:
            try:
                square = int(input("Wprowadz numer kwadratu: "))
                field = int(input("Wprowadz numer kolumny w kwadracie: "))
                try:
                    if self.board.areas[square][field] == ' ':
                        if self.board.areas[square] in self.computer.winned_squares or\
                                self.board.areas[square] in self.player.winned_squares:
                            print("This square is already winned")
                            continue
                        else:
                            self.board.set(square, field, self.player.sign)
                            return square
                    else:
                        print("This field is filled")
                except IndexError:
                    print("Must be a number from 0 to 8")
            except ValueError:
                continue

    def computer_move(self):
        while True:
            square = randint(0, 8)
            field = randint(0, 8)
            if self.board.areas[square][field] == ' ':
                if self.board.areas[square] in self.computer.winned_squares or\
                            self.board.areas[square] in self.player.winned_squares:
                    continue
                self.board.set(square, field, self.computer.sign)
                return square
