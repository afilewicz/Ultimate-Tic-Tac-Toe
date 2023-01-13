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
sign = 'X'
player = Player('Adam')
player.set_sign(sign)
computer = AI()
game = Game(player, computer)
round = 0
board = game.board
while game.result is None:
    board.draw_board()
    for person in game.players:
        while True:
            try:
                if person == player:
                    square = int(input("Wprowadź numer kwadratu: "))
                    field = int(input("Wprowadź numer kwadratu w kwadracie: "))
                else:
                    # square = randint(0, 8)
                    # field = randint(0, 8)
                    if board.areas[square].check_which_better(game.player, game.computer):
                        square, field = game.computer.defense(board, square, game.player)
                    else:
                        square, field = game.computer.offense(board, player)
                try:
                    if board.areas[square].check_if_not_filled(field):
                        if board.check_if_winned(square):
                            if person == player:
                                print("Ten kwadrat jest już wygrany")
                                continue
                        else:
                            board.areas[square].set(field, person.sign)
                            round += 1
                            break
                    else:
                        if person == player:
                            print("To pole jest już zapełnione")
                except IndexError:
                    print("Podaj numer od 0 do 8")
            except ValueError:
                continue
        if board.as_a_small.check_if_not_full():
            if board.areas[square].checking_if_win_square(person):
                person.winned_squares.append(board.areas[square])
                board.as_a_small.set(square, person.sign)
                if board.as_a_small.checking_if_win_square(person):
                    game._winner = person
                    game._result = True
        else:
            game._result = False
board.draw_board()
if game.result is True:
    print(f"Zwycięzcą został/a {game.winner.name}")
else:
    print("Nie ma zwycięzcy")
sleep(5)
# usuniecie ruchu komputera po ewentualnej wygranej przeze mnie
