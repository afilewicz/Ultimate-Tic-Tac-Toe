class EmptyNameError(Exception):
    def __init__(self):
        super().__init__('Name cannot be empty')


class InvalidSignError(Exception):
    pass


class Player:
    def __init__(self, name='', sign='X'):
        if name:
            self._name = name
        else:
            raise EmptyNameError
        if sign not in ['X', 'O']:
            raise InvalidSignError("Sign must be a 'X' or 'O'")
        else:
            self._sign = sign

    @property
    def name(self):
        return self._name

    @property
    def sign(self):
        return self._sign

    def move(self, column, row):
        return column, row
