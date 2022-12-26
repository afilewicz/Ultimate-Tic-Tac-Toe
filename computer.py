from random import randint


class Computer:
    def __init__(self):
        self._sign = ''
        self.winned_squares = []

    @property
    def sign(self):
        return self._sign

    def set_sign(self, sign):
        self._sign = sign

    def move(self, game):
        while True:
            square = randint(0, 8)
            field = randint(0, 8)
            if game.board.areas[square][field] == ' ':
                if square in self.winned_squares or\
                            square in game.player.winned_squares:
                    continue
                game.board.set(square, field, self.sign)
                return square
