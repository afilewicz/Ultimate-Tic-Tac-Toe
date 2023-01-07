from player import Player
# from computer import Computer
from game import Game
from time import sleep
from random import randint
from AI import AI


class EmptyNameError(Exception):
    def __init__(self):
        super().__init__('Name cannot be empty')


class InvalidSignError(Exception):
    pass


# print("Enter your name:")
# name = input()
# if not name:
#     raise EmptyNameError
# print("Enter your sign. Must be 'X' or 'O'")
# sign = input()
# sign = sign.upper()
# if sign not in ['X', 'O']:
#     raise InvalidSignError("Sign must be a 'X' or 'O'")
player = Player(name='Adam', sign='X')
computer = AI()
game = Game(player, computer)
while game.result is None:
    game.board.draw_board()
    for person in game.players:
        while True:
            try:
                if person == player:
                    square = int(input("Wprowadz numer kwadratu: "))
                    field = int(input("Wprowadz numer kolumny w kwadracie: "))
                else:
                    square = randint(0, 8)
                    field = randint(0, 8)
                    # square, field = AI.defense(square, field, game.board, game.player)
                try:
                    if game.check_if_not_filled(square, field):
                        if game.check_if_winned(square):
                            if person == player:
                                print("This square is already winned")
                            continue
                        else:
                            game.board.set(square, field, person.sign)
                            break
                    else:
                        if person == player:
                            print("This field is filled")
                except IndexError:
                    print("Must be a number from 0 to 8")
            except ValueError:
                continue
        if game.checking_if_win_square(person, square):
            if game.checking_if_win_square(person, game.board):
                if person == game.player:
                    game._result = True
                else:
                    game._result = False
game.board.draw_board()
if game.result is True:
    print(f"The winner is {player.name}")
else:
    print("The winner is computer")
sleep(5)
