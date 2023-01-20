class Player:
    """
    Makes an instantion of player.
    """
    def __init__(self, name):
        if not name:
            self._name = 'gracz'
        else:
            self._name = name
        self._sign = None

    @property
    def name(self):
        return self._name

    @property
    def sign(self):
        return self._sign

    @sign.setter
    def sign(self, new_sign):
        self._sign = new_sign
