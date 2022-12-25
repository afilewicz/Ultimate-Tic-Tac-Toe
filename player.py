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

    def move(self, game):
        while True:
            try:
                print("Wprowadz numer kwadratu:")
                square = int(input())
                print("Wprowadz numer kolumny w kwadracie:")
                field = int(input())
            except ValueError:
                continue
            try:
                if game.board.areas[square][field] == ' ':
                    if square in game.board.winned_squares_computer or square in game.board.winned_squares_player:
                        print("This square is already winned")
                        continue
                    else:
                        game.board.set(square, field, self.sign)
                        return square
                else:
                    print("This field is filled")
            except IndexError:
                print("Must be a number from 0 to 8")

# ValueError przy nacisnieciu entera
