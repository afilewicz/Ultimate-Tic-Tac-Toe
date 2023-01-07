from board import BigBoard, dimension
from player import Player
from computer import Computer


class Game:
    def __init__(self, player: Player, computer: Computer):
        self.board = BigBoard()
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
        if square != self.board:
            fields = person.sign
            board = self.board.areas[square]
            board.areas = self.board.areas[square]._single_arr
        else:
            fields = person.winned_squares
            board = self.board
        columns = []
        rows = []
        diagonals = [0, 0]
        for i in range(dimension):
            columns.append(0)
            rows.append(0)
        for i, field in enumerate(board.areas):
            if field in fields:
                for number in range(dimension):
                    if i % dimension == number:
                        columns[number] += 1
                    if i // dimension == number:
                        rows[number] += 1
                if (i % dimension + i // dimension) == (dimension-1):
                    diagonals[1] += 1
                if i % (dimension+1) == 0:
                    diagonals[0] += 1
        any = columns + rows + diagonals
        for counter in any:
            if counter == dimension:
                person.winned_squares.append(board)
                return True

    def check_if_not_filled(self, square, field):
        if self.board.areas[square]._single_arr[field] == ' ':
            return True
        else:
            return False

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
