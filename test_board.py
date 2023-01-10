from board import BigBoard, dimension


def test_board_init():
    board = BigBoard()
    assert len(board.areas) == dimension**2
    for area in board.areas:
        assert len(area.single_arr) == dimension**2


def test_set():
    board = BigBoard()
    board.set(1, 7, 'O')
    assert board.areas[1].areas[7] == 'O'
