from board import BigBoard, Single_Board
from constants import dimension
from player import Player
from AI import AI

player = Player('Adam')
player.set_sign('X')
computer = AI()
computer.set_sign('O')


def test__big_board_init():
    Bigboard = BigBoard()
    assert len(Bigboard.areas) == dimension**2
    for area in Bigboard.areas:
        assert len(area.areas) == dimension**2


def test_init_single_board():
    board = Single_Board()
    assert len(board.areas) == dimension**2
    for area in board.areas:
        assert area == ' '


def test_set():
    board = Single_Board()
    board.set(7, 'O')
    assert board.areas[7] == 'O'


def test_check_if_not_filled():
    board = Single_Board()
    board.set(6, 'O')
    assert board.check_if_not_filled(7) is True
    assert board.check_if_not_filled(6) is False


def test_check_if_not_full():
    board = Single_Board()
    for field in range(dimension**2):
        board.set(field, 'X')
    assert board.check_if_not_full() is False


def test_check_if_not_full_true():
    board = Single_Board()
    for field in range(dimension**2-1):
        board.set(field, 'X')
    assert board.check_if_not_full() is True


def test_check_how_many_in_sequence_column_2_filled():
    board = Single_Board()
    for i in range(dimension**2):
        if i % dimension == 2:
            board.set(i, player.sign)
    assert board.check_how_many_in_sequence(player)[2] == dimension
    for i in range(dimension):
        assert board.check_how_many_in_sequence(player)[dimension+i] == 1
    assert board.check_how_many_in_sequence(player)[-1] == 1
    assert board.check_how_many_in_sequence(player)[-2] == 1


def test_checking_if_win_square():
    board = Single_Board()
    for i in range(dimension**2):
        if i % dimension == 2:
            board.set(i, player.sign)
    assert board.checking_if_win_square(player) is True


def test_checking_if_win_square_false():
    board = Single_Board()
    board.set(5, player.sign)
    assert board.checking_if_win_square(player) is False


def test_search_max_list():
    board = Single_Board()
    for i in range(dimension**2):
        if i % dimension == 2:
            board.set(i, player.sign)
    assert board.search_max_list(player)[0] == [2]
    assert board.search_max_list(player)[1] == dimension


def test_search_max_list_diagonal_0():
    board = Single_Board()
    for i in range(dimension**2-1):
        if i % (dimension + 1) == 0:
            board.set(i, player.sign)
    assert board.search_max_list(player)[0] == [2*dimension]
    assert board.search_max_list(player)[1] == dimension-1


def test_check_which_better_default_true():
    board = BigBoard()
    for i in range(dimension**2-1):
        if i % (dimension + 1) == 0:
            board.areas[3].set(i, player.sign)
    assert board.areas[3].check_which_better(player, computer) is True


def test_check_which_better_default_false():
    board = BigBoard()
    board.areas[0].set(0, player.sign)
    assert board.areas[0].check_which_better(player, computer) is False


def test_check_which_better_if_cannot_cover():
    board = BigBoard()
    for i in range(dimension**2-dimension):
        if i % (dimension + 1) == 0 or i % dimension == 0:
            board.areas[2].set(i, player.sign)
    assert board.areas[2].check_which_better(player, computer) is False


def test_check_which_better_if_win_after_attack():
    board = BigBoard()
    for i in range(dimension**2-1):
        if i % (dimension + 1) == 0:
            board.areas[2].set(i, computer.sign)
        if i // dimension == dimension-1:
            board.areas[2].set(i, player.sign)
    assert board.areas[2].check_which_better(player, computer) is False


def test_check_if_winned():
    board = BigBoard()
    board.as_a_small.set(5, AI)
    assert board.check_if_winned(5) is True


def test_check_if_winned_false():
    board = BigBoard()
    board.as_a_small.set(5, AI)
    assert board.check_if_winned(4) is False
