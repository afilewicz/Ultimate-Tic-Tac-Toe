class Player:
    def __init__(self, name):
        self._name = name
        self._sign = None
        self.winned_squares = []

    @property
    def name(self):
        return self._name

    @property
    def sign(self):
        return self._sign

    def set_sign(self, sign):
        self._sign = sign
