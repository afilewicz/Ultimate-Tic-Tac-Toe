from AI import AI, make_dict_of_answers
from board import BigBoard
from constants import DIMENSION
from player import Player

player = Player('Adam')
player.sign = 'X'


def test_make_dict_of_answers_3():
    if DIMENSION == 3:
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
    computer.sign = 'X'
    assert computer.name == 'komputer'
    assert computer.sign == 'X'


def test_defense():
    computer = AI()
    board = BigBoard()
    for i in range(DIMENSION**2-1):
        if i % (DIMENSION + 1) == 0:
            board.areas[3].set(i, player.sign)
    assert computer.defense(board, 3, player) == (3, DIMENSION**2-1)


def test_choose_square_default():
    computer = AI()
    board = BigBoard()
    board.areas[4].set(5, computer.sign)
    assert computer.choose_square(board) == 4


def test_choose_square_after_defense():
    computer = AI()
    board = BigBoard()
    board.areas[0].set(DIMENSION, computer.sign)
    for i in range(DIMENSION**2-1):
        if i % DIMENSION == 1:
            board.areas[3].set(i, player.sign)
    board.areas[3].set(DIMENSION, computer.sign)
    board.areas[3].set(0, player.sign)
    assert computer.choose_square(board) in [0, 3]


def test_choose_field_in_square():
    computer = AI()
    board = BigBoard()
    for i in range(DIMENSION**2-DIMENSION):
        if i % DIMENSION == 1:
            board.areas[3].set(i, computer.sign)
    assert computer.choose_field_in_square(board.areas[3])\
        == DIMENSION*(DIMENSION-1) + 1
