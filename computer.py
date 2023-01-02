class Computer:
    def __init__(self):
        self._sign = ''
        self.winned_squares = []

    @property
    def sign(self):
        return self._sign

    def set_sign(self, sign):
        self._sign = sign
