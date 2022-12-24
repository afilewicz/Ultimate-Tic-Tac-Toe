from player import Player
from computer import Computer
from game import Game


player = Player('Adam')
computer = Computer('O')
game = Game(player, computer)
while game.result is None:
    game.board.make_board()
    print("Wprowadz numer kwadratu:")
    x = int(input())
    print("Wprowadz numer kolumny w kwadracie:")
    y = int(input())
    game.round(x, y)
if game.result is True:
    print(f"The winner is {player.name}")
else:
    print("The winner is computer")
