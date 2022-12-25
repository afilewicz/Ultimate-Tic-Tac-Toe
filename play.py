from player import Player
from computer import Computer
from game import Game


player = Player('Adam')
computer = Computer('O')
game = Game(player, computer)
while game.result is None:
    game.round()
if game.result is True:
    print(f"The winner is {player.name}")
else:
    print("The winner is computer")
