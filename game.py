from board import BigBoard
from player import Player
from computer import Computer


class Game:
    def __init__(self, player: Player, computer: Player):
        self.board = BigBoard()
        self._player = player
        self._computer = computer
        self._players = [player, computer]
        self._result = None
        if self.player.sign == 'X':
            self.computer._sign = 'O'
        else:
            self.computer._sign = 'X'
        self._winner = None

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

    @property
    def winner(self):
        return self._winner

    def check_if_winned(self, square):
        if self.board.areas[square] in self.computer.winned_squares or\
                self.board.areas[square] in self.player.winned_squares:
            return True
        else:
            return False

    # def player_move(self):
    #     while True:
    #         try:
    #             square = int(input("Wprowadz numer kwadratu: "))
    #             field = int(input("Wprowadz numer kolumny w kwadracie: "))
    #             try:
    #                 if self.board.areas[square][field] == ' ':
    #                     if self.board.areas[square] in self.computer.winned_squares or\
    #                             self.board.areas[square] in self.player.winned_squares:
    #                         print("This square is already winned")
    #                         continue
    #                     else:
    #                         self.board.set(square, field, self.player.sign)
    #                         return square
    #                 else:
    #                     print("This field is filled")
    #             except IndexError:
    #                 print("Must be a number from 0 to 8")
    #         except ValueError:
    #             continue

    # def computer_move(self):
    #     while True:
    #         square = randint(0, 8)
    #         field = randint(0, 8)
    #         if self.board.areas[square][field] == ' ':
    #             if self.board.areas[square] in self.computer.winned_squares or\
    #                         self.board.areas[square] in self.player.winned_squares:
    #                 continue
    #             self.board.set(square, field, self.computer.sign)
    #             return square
