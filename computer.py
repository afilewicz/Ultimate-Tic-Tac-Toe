from random import randint


class Computer:
    def __init__(self, sign):
        self._sign = sign

    @property
    def sign(self):
        return self._sign

    def move(self, game):
        while 1:
            square = randint(0, 8)
            field = randint(0, 8)
            if game.board.areas[square][field] == ' ':
                game.board.set(square, field, self.sign)
                return square
