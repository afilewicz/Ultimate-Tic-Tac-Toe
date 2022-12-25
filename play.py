from player import Player
from computer import Computer
from game import Game

print("Enter your name:")
name = input()
print("Enter your sign. Must be 'X' or 'O'")
sign = input()
player = Player(name, sign)
computer = Computer()
game = Game(player, computer)
while game.result is None:
    game.round()
game.board.draw_board()
if game.result is True:
    print(f"The winner is {player.name}")
else:
    print("The winner is computer")
