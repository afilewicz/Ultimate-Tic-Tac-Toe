from player import Player
from computer import Computer
from game import Game
from time import sleep
from AI import AI


class InvalidSignError(Exception):
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
    player = Player(name)
    player.set_sign(sign)
    print("Jeśli chcesz grać z komputerm, którego ruchy są losowe napisz 'losowy':")
    choose = input()
    if choose == 'losowy':
        computer = Computer()
    else:
        computer = AI()
    game = Game(player, computer)
    board = game.board
    while game.result is None:
        for person in game.players:
            while True:
                try:
                    if person == player:
                        board.draw_board()
                        square = int(input("Wprowadź numer kwadratu: "))
                        field = int(input("Wprowadź numer kwadratu w kwadracie: "))
                    elif type(computer) == AI:
                        if board.areas[square].check_which_better(game.player, game.computer):
                            sequence_number = board.areas[square].check_which_better(game.player, game.computer)[1]
                            square, field = game.computer.defense(board, square, sequence_number)
                        else:
                            square, field = game.computer.offense(board)
                    else:
                        square, field = computer.random_move(board)
                    try:
                        if board.areas[square].check_if_not_filled(field):
                            if board.check_if_winned(square):
                                if person == player:
                                    print("Ten kwadrat jest już wygrany")
                                    continue
                            else:
                                board.areas[square].set(field, person.sign)
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
                    board.as_a_small.set(square, person.sign)
                    print(f"Kwadrat nr {square} został wygrany.")
                    if board.as_a_small.checking_if_win_square(person):
                        game._winner = person
                        game._result = True
                        break
                if not board.areas[square].check_if_not_full()\
                        and board.as_a_small.areas[square] == ' ':
                    board.as_a_small.set(square, 'full')
                    print('Kwadrat zremisowany')
                if not board.as_a_small.check_if_not_full():
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
