from player import Player
from random import randint
from constants import dimension


class Computer(Player):
    def __init__(self):
        super().__init__('komputer')

    def random_move(self, board):
        list_of_squares = []
        list_of_fields = []
        for i in range(dimension**2):
            list_of_squares.append(i)
            list_of_fields.append(i)
        while True:
            square = randint(0, dimension**2-1)
            if board.as_a_small.check_if_not_filled(square):
                field = randint(0, dimension**2-1)
                if board.areas[square].check_if_not_filled(field):
                    return square, field
                else:
                    list_of_fields.remove(field)
            else:
                list_of_squares.remove(square)
