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
    name = input("Wprowadź swoje imię: ")
    while True:
        try:
            print("Wpisz swój znak. Ma to być 'X' lub 'O'")
            sign = input()
            sign = sign.upper()
            if sign not in ['X', 'O']:
                raise InvalidSignError("Sign must be a 'X' or 'O'")
            else:
                break
        except InvalidSignError:
            pass
    person = Player(name)
    print("Jeśli chcesz grać z komputerem, \
którego ruchy są losowe napisz 'losowy':")
    choose = input()
    if choose == 'losowy':
        computer = Computer()
    else:
        computer = AI()
    game = Game(person, computer, sign)
    board = game.board
    while game.result is None:
        for player in game.players:
            while True:
                try:
                    if player == person:
                        board.draw_board()
                        square = int(input("Wprowadź numer kwadratu: "))
                        field = int(input("Wprowadź numer pola w kwadracie: "))
                    elif type(computer) == AI:
                        if board.areas[square].check_which_better(game.player, game.computer):
                            square, field = game.computer.defense(board, square, game.player)
                        else:
                            square, field = game.computer.offense(board)
                    else:
                        square, field = computer.random_move(board)
                    try:
                        if not board.areas[square].filled(field):
                            if board.check_if_winned(square):
                                if player == person:
                                    print("Ten kwadrat jest już wygrany")
                                    continue
                            else:
                                board.areas[square].set(field, player.sign)
                                break
                        else:
                            if player == person:
                                print("To pole jest już zapełnione")
                    except IndexError:
                        print("Podaj numer od 0 do 8")
                except ValueError:
                    continue
            if not board.as_a_small.full():
                if board.areas[square].checking_if_win_square(player):
                    board.as_a_small.set(square, player.sign)
                    print(f"Kwadrat nr {square} został wygrany.")
                    if board.as_a_small.checking_if_win_square(player):
                        game._winner = player
                        game._result = True
                        break
                if board.areas[square].full()\
                        and board.as_a_small.areas[square] == ' ':
                    board.as_a_small.set(square, 'full')
                    print('Kwadrat zremisowany')
                if board.as_a_small.full():
                    game._result = False
                    break
    board.draw_board()
    if game.result is True:
        print(f"Zwycięzcą został/a {game.winner.name}")
    else:
        print("Nie ma zwycięzcy")
    sleep(5)


if __name__ == "__main__":
    main()
