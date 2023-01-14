from game import Game
from player import Player
from AI import AI
from board import BigBoard


def test_init_game():
    player = Player("Adam")
    player.set_sign("X")
    computer = AI()
    game = Game(player, computer)
    assert type(game.board) == BigBoard
    assert game.player.sign == "X"
    assert game.computer.sign == "O"
    assert game.players == [player, computer]
    assert game.result is None
    assert game.winner is None
