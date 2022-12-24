from random import randint


class Computer:
    def __init__(self, sign):
        self._sign = sign

    @property
    def sign(self):
        return self._sign

    def move(self):
        row = randint(0, 8)
        column = randint(0, 8)
        return column, row
