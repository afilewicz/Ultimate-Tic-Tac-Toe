from player import Player
from random import randint
from constants import DIMENSION


class Computer(Player):
    """
    Makes an instance of computer player that makes random moves.
    """
    def __init__(self):
        super().__init__('komputer')

    def random_move(self, board):
        """
        Returns random square and field on the board which is not filled.
        """
        list_of_squares = []
        list_of_fields = []
        for i in range(DIMENSION**2):
            list_of_squares.append(i)
            list_of_fields.append(i)
        while True:
            square = randint(0, DIMENSION**2-1)
            if not board.as_a_small.filled(square):
                field = randint(0, DIMENSION**2-1)
                if not board.areas[square].filled(field):
                    return square, field
                else:
                    list_of_fields.remove(field)
            else:
                list_of_squares.remove(square)
