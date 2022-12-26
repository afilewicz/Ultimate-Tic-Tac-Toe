from board import Board


def test_board_init():
    board = Board()
    assert len(board.areas) == 9
    for area in board.areas:
        assert len(area) == 9


def test_set():
    board = Board()
    square = 1
    mini_square = 7
    sign = 'O'
    board.set(square, mini_square, sign)
    assert board.areas[1][7] == 'O'
