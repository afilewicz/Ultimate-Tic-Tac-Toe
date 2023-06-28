from player import Player
from computer import Computer
from game import Game
from time import sleep
from AI import AI


class InvalidSignError(Exception):

    """ Description

    Raises when sign is incorrect.

    """
    pass


def main():
    square = 0
    print("Wprowadź swoje imie: ")
    name = input()
    while True:
        try:
            print("Wpisz swój znak. Ma to być 'X' lub 'O': ")
            sign = input()
            sign = sign.upper()
            if sign not in ['X', 'O']:
                raise InvalidSignError("Sign must be a 'X' or 'O'")
            else:
                break
        except InvalidSignError:
            pass
    person = Player(name)
    print("\nJeśli chcesz grać z komputerem, \
którego ruchy są losowe napisz 'l': ")
    choose = input()
    if choose == 'l':
        computer = Computer()
    else:
        computer = AI()
    game = Game(person, computer, sign)
    board = game.board


    while game.result is None:
        for player in game.players:
            while True:
                if player == person:
                    try:
                        board.draw_board()
                        square = int(input("Wprowadź numer kwadratu: "))
                        field = int(input("Wprowadź numer pola w kwadracie: "))
                        try:
                            if not board.areas[square].filled(field):
                                if board.check_if_winned(square):
                                    print("\nTen kwadrat jest już wygrany")
                                    continue
                                else:
                                    board.areas[square].set(field, player.sign)
                                    break
                            else:
                                print("\nTo pole jest już zapełnione")
                        except IndexError:
                            print("\nPodaj numer od 0 do 8")
                    except ValueError:
                        continue
                else:
                    if type(computer) == AI:
                        square, field = game.AI_move(square)
                        break
                    else:
                        square, field = game.computer_move()
                        break
            if (game.check_if_end(square, player)):
                break

    board.draw_board()
    if game.result is True:
        print(f"\nZwycięzcą został/a {game.winner.name}")
    else:
        print("\nNie ma zwycięzcy")
    sleep(5)


if __name__ == "__main__":
    main()
