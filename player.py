class Player:
    def __init__(self, name, sign):
        self._name = name
        self._sign = sign
        self.winned_squares = []

    @property
    def name(self):
        return self._name

    @property
    def sign(self):
        return self._sign
