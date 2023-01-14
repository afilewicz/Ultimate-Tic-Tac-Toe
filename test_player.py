from player import Player
# import pytest


# def test_player_default():
#     player = Player('Adam')
#     assert player.name == 'Adam'
#     assert player.sign == 'X'


def test_player():
    player = Player('Adam', 'O')
    assert player.name == 'Adam'
    assert player.sign == 'O'


# def test_init_player_no_name():
#     with pytest.raises(EmptyNameError):
#         Player()


# def test_init_player_invalid_sign():
#     with pytest.raises(InvalidSignError):
#         Player('Adam', '@')


# def test_player_move():
#     player = Player('Adam', 'O')
#     game = Game(player, computer=Computer)
#     square = 7
#     field = 3
#     player.move(game)
