from AI import AI, make_dict_of_answers
from board import BigBoard
from constants import dimension
from player import Player

player = Player('Adam')
player.set_sign('X')


def test_make_dict_of_answers_3():
    if dimension == 3:
        answers_2 = make_dict_of_answers()
        assert answers_2 == {
            0: [0, 3, 6],
            1: [1, 4, 7],
            2: [2, 5, 8],
            3: [0, 1, 2],
            4: [3, 4, 5],
            5: [6, 7, 8],
            6: [0, 4, 8],
            7: [2, 4, 6]
        }


def test_computer_init():
    computer = AI()
    computer.set_sign('X')
    assert computer.name == 'komputer'
    assert computer.sign == 'X'


def test_defense():
    computer = AI()
    board = BigBoard()
    for i in range(dimension**2-1):
        if i % (dimension + 1) == 0:
            board.areas[3].set(i, player.sign)
    assert computer.defense(board, 3, 2*dimension) == (3, dimension**2-1)


def test_choose_square_default():
    computer = AI()
    board = BigBoard()
    board.areas[4].set(5, computer.sign)
    assert computer.choose_square(board) == 4


def test_choose_square_after_defense():
    computer = AI()
    board = BigBoard()
    board.areas[0].set(dimension, computer.sign)
    for i in range(dimension**2-1):
        if i % dimension == 1:
            board.areas[3].set(i, player.sign)
    board.areas[3].set(dimension, computer.sign)
    board.areas[3].set(0, player.sign)
    assert computer.choose_square(board) in [0, 3]


def test_choose_field_in_square():
    computer = AI()
    board = BigBoard()
    for i in range(dimension**2-dimension):
        if i % dimension == 1:
            board.areas[3].set(i, computer.sign)
    assert computer.choose_field_in_square(board.areas[3]) == dimension*(dimension-1) + 1

#początkowo funkcja miala atakować, gdy nie może się bronić,\
#  jednak wtedy zostawialo puste pole gdy dwie sekwencje przechodzily przez te samo pole


# def test_choose_field_in_square_from_practising():
#     computer = AI()
#     board = BigBoard()
#     computer_signs = [0, 6]
#     player_signs = [2, 3, 4, 8]
#     for field in player_signs:
#         board.areas[3].set(field, player.sign)
#     for field in computer_signs:
#         board.areas[3].set(field, computer.sign)
#     assert board.areas[3].check_which_better(player, computer) is True
#     assert computer.defense(board, 3, player) == (3, 5)
