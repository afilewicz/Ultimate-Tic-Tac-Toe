from player import Player
from computer import Computer
from game import Game
from time import sleep


class EmptyNameError(Exception):
    def __init__(self):
        super().__init__('Name cannot be empty')


class InvalidSignError(Exception):
    pass


print("Enter your name:")
name = input()
if not name:
    raise EmptyNameError
print("Enter your sign. Must be 'X' or 'O'")
sign = input()
sign = sign.upper()
if sign not in ['X', 'O']:
    raise InvalidSignError("Sign must be a 'X' or 'O'")
player = Player(name, sign)
computer = Computer()
game = Game(player, computer)
while game.result is None:
    game.board.draw_board()
    square = game.player_move()
    if game.checking_if_win_square(player, square):
        player.winned_squares.append(game.board.areas[square])
        if game.checking_if_win_square(player, game.board.areas):
            game._result = True
    square_com = game.computer_move()
    if game.checking_if_win_square(computer, square_com):
        player.winned_squares.append(game.board.areas[square])
        if game.checking_if_win_square(player, game.board.areas):
            game._result = False

game.board.draw_board()
if game.result is True:
    print(f"The winner is {player.name}")
else:
    print("The winner is computer")
sleep(5)
