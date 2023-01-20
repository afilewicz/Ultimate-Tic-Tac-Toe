from board import BigBoard
from player import Player
from random import shuffle
from colored import fg, attr
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
        self.player.sign = fg(2)+str(self.player.sign.name)+attr('reset')
        self.computer.sign = fg(1)+str(self.computer.sign.name)+attr('reset')
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
