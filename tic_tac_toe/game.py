from board import BigBoard
from player import Player
from random import shuffle
from sign import Sign


class Game:

    """ Description

    Class of the game.

    """
    def __init__(self, player: Player, computer: Player, sign):

        """ Description

        Class game assigns chosen sign as a player sign and the other one
        as a computer sign.
        :type player: Player
        :param player:

        :type computer: Player
        :param computer:

        :type sign: Sign, string
        :param sign:

        """
        self.board = BigBoard()
        self._player = player
        self._computer = computer
        self._players = [player, computer]
        shuffle(self._players)
        if sign == 'X':
            self.computer.sign = Sign.O
            self.player.sign = Sign.X
        else:
            self.player.sign = Sign.O
            self.computer.sign = Sign.X
        self.player.sign = str(self.player.sign.name)
        self.computer.sign = str(self.computer.sign.name)
        self._result = None
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

    def computer_move(self):
        square, field = self.computer.random_move(self.board)
        if not self.board.areas[square].filled(field):
            if not self.board.check_if_winned(square):
                self.board.areas[square].set(field, self.computer.sign)
                return square, field
        else:
            self.computer_move()

    def AI_move(self, square):
        if self.board.areas[square].check_which_better(self.player, self.computer):
            square, field = self.computer.defense(self.board, square, self.player)
        else:
            square, field = self.computer.offense(self.board)
        if not self.board.areas[square].filled(field):
            if self.board.check_if_winned(square):
                self.AI_move(square)
            else:
                self.board.areas[square].set(field, self.computer.sign)
                return square, field

    def check_if_end(self, square, player):
        if not self.board.as_a_small.full():
            if self.board.areas[square].checking_if_win_square(player):
                self.board.as_a_small.set(square, player.sign)
                print(f"\nKwadrat nr {square} został wygrany.")
                if self.board.as_a_small.checking_if_win_square(player):
                    self._winner = player
                    self._result = True
                    return True
            if self.board.areas[square].full()\
                    and self.board.as_a_small.areas[square] == ' ':
                self.board.as_a_small.set(square, 'full')
                print("\nKwadrat zremisowany")
            if self.board.as_a_small.full():
                self._result = False
        return (self._result is not None)
