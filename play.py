from player import Player
# from computer import Computer
from game import Game
from time import sleep
from random import randint
from AI import AI
from check import check_which_better, checking_if_win_square, check_if_not_filled
from check import check_if_not_a_draw


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
round = 0
while game.result is None:
    game.board.draw_board()
    for person in game.players:
        while True:
            try:
                if person == player:
                    square = int(input("Wprowadz numer kwadratu: "))
                    field = int(input("Wprowadz numer kwadratu w kwadracie: "))
                else:
                    # square = randint(0, 8)
                    # field = randint(0, 8)
                    if check_which_better(game.board, square, game.player, game.computer):
                        square, field = game.computer.defense(game.board, square, game.player)
                    else:
                        square, field = game.computer.offense(game.board, player)
                try:
                    if check_if_not_filled(game.board, square, field):
                        if game.check_if_winned(square):
                            if person == player:
                                print("This square is already winned")
                                continue
                            # else:
                            #     if not check_which_better(game.board, square, game.player):
                            #         square, field = game.computer.defense(game.board, square, game.player)
                            #     else:
                            #         square, field = game.computer.offense(game.board)
                        else:
                            game.board.set(square, field, person.sign)
                            round += 1
                            break
                    else:
                        if person == player:
                            print("This field is filled")
                except IndexError:
                    print("Must be a number from 0 to 8")
            except ValueError:
                continue
        if check_if_not_a_draw(game.board):
            if checking_if_win_square(game.board, person, square):
                person.winned_squares.append(game.board.areas[square])
                if checking_if_win_square(game.board, person):
                    game._winner = person
                    game._result = True
        else:
            game._result = False
game.board.draw_board()
if game.result is True:
    print(f"The winner is {game.winner.name}")
else:
    print("The winner is computer")
sleep(5)
