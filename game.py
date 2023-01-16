from board import BigBoard
from player import Player
from random import shuffle


class Game:
    def __init__(self, player: Player, computer: Player):
        self.board = BigBoard()
        self._player = player
        self._computer = computer
        self._players = [player, computer]
        shuffle(self._players)
        if self.player.sign == 'X':
            self.computer._sign = 'O'
        else:
            self.computer._sign = 'X'
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
