from player import Player


def test_player():
    player = Player('Adam')
    assert player.name == 'Adam'


def test_set_sign():
    player = Player('Adam')
    player.sign = 'X'
    assert player.sign == 'X'
