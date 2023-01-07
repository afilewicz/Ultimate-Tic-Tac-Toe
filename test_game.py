from game import Game
from player import Player
from computer import Computer
from board import BigBoard, dimension


def test_init_game():
    game = Game(player=Player("Adam", "X"), computer=Computer())
    assert type(game.board) == BigBoard
    assert game.player.sign == "X"
    assert game.computer.sign == "O"
    assert game.result is None


def test_checking_if_win_square_column():
    game = Game(player=Player("Adam", "X"), computer=Computer())
    for field in range(dimension**2):
        if field % dimension == 2:
            game.board.set(3, field, "X")
    assert game.checking_if_win_square(game.player, 3) is True
    assert game.player.winned_squares == [game.board.areas[3]]


def test_checking_if_win_square_row():
    game = Game(player=Player("Adam", "X"), computer=Computer())
    row_1 = [4, 3, 5]
    for field in row_1:
        game.board.set(6, field, "X")
    assert game.checking_if_win_square(game.player, 6) is True
    assert game.player.winned_squares == [game.board.areas[6]]


def test_checking_if_win_square_diagonal_1():
    game = Game(player=Player("Adam", "O"), computer=Computer())
    game.board.set(7, 8, "X")
    game.board.set(7, 4, "X")
    game.board.set(7, 0, "X")
    assert game.checking_if_win_square(game.computer, 7) is True
    assert game.computer.winned_squares == [game.board.areas[7]]


def test_checking_if_win_square_diagonal_2():
    game = Game(player=Player("Adam", "X"), computer=Computer())
    game.board.set(1, 2, "X")
    game.board.set(1, 4, "X")
    game.board.set(1, 6, "X")
    assert game.checking_if_win_square(game.player, 1) is True
    assert game.player.winned_squares == [game.board.areas[1]]


def test_checking_if_win_big_square():
    game = Game(player=Player("Adam", "X"), computer=Computer())
    game.player.winned_squares = [game.board.areas[2], game.board.areas[5], game.board.areas[8]]
    # game.board.set(2, 5, "X")
    # game.board.set(2, 8, "X")
    # game.board.set(2, 2, "X")
    # game.board.set(5, 4, "X")
    # game.board.set(5, 0, "X")
    # game.board.set(5, 8, "X")
    # game.board.set(8, 3, "X")
    # game.board.set(8, 4, "X")
    # game.board.set(8, 5, "X")
    # game.checking_if_win_square(game.player, 2)
    # game.checking_if_win_square(game.player, 5)
    # game.checking_if_win_square(game.player, 8)
    assert game.checking_if_win_square(game.player, game.board) is True
    assert game.player.winned_squares == [game.board.areas[2], game.board.areas[5], game.board.areas[8], game.board]


def test_check_if_not_filled_true():
    game = Game(player=Player("Adam", "O"), computer=Computer())
    assert game.check_if_not_filled(1, 2) is True


def test_check_if_not_filled_false():
    game = Game(player=Player("Adam", "O"), computer=Computer())
    game.board.set(1, 2, "X")
    assert game.check_if_not_filled(1, 2) is False


def test_check_if_winned_false():
    game = Game(player=Player("Adam", "O"), computer=Computer())
    assert game.check_if_winned(1) is False


def test_check_if_winned_true():
    game = Game(player=Player("Adam", "O"), computer=Computer())
    game.player.winned_squares = [game.board.areas[1]]
    assert game.check_if_winned(1) is True
