from computer import Computer
from random import choice, randint
from board import dimension
from check import check, search_max, checking_if_win_square, check_if_not_filled
from check import check_if_not_full
answers_2 = {
    0: [0, 3, 6],
    1: [1, 4, 7],
    2: [2, 5, 8],
    3: [0, 1, 2],
    4: [3, 4, 5],
    5: [6, 7, 8],
    6: [0, 4, 8],
    7: [2, 4, 6]
}

moves = {
    0: [0, 3, 6],
    1: [1, 3],
    2: [2, 3, 7],
    3: [0, 4],
    4: [1, 4, 6, 7],
    5: [2, 4],
    6: [0, 5, 7],
    7: [1, 5],
    8: [2, 5, 6]
}


class AI(Computer):
    def __init__(self):
        super().__init__()
        self.player_moves = []
        self.moves = []
        for square in range(dimension**2):
            self.player_moves.append([])
            self.moves.append([])
            for field in range(dimension**2):
                self.player_moves[square].append([])

    def defense(self, board, square, player):
        if checking_if_win_square(board, player, square) or\
                checking_if_win_square(board, self, square):
            com_square = randint(0, dimension**2)
        else:
            com_square = square
        player_max = search_max(board, square, player)
        com_field = choice(answers_2[choice(player_max)])
        return com_square, com_field

    def offense(self, board, player):
        answers = {
    0: [0, 3, 6],
    1: [1, 4, 7],
    2: [2, 5, 8],
    3: [0, 1, 2],
    4: [3, 4, 5],
    5: [6, 7, 8],
    6: [0, 4, 8],
    7: [2, 4, 6]
}
        list_of_signed = []
        list_of_signed_two_times = []
        list_of_not_full = []
        for index in range(dimension**2):
            if checking_if_win_square(board, player, index) or\
                    checking_if_win_square(board, self, index):
                continue
            else:
                if check_if_not_full(board, index):
                    max_from_square_list = search_max(board, index, self)
                    list_of_not_full.append(index)
                    if len(max_from_square_list) == (2*dimension+1):
                        list_of_signed.append(index)
                    if len(max_from_square_list) < (2*dimension+1):
                        list_of_signed_two_times.append(index)
        if len(list_of_signed_two_times) == 0:
            if len(list_of_signed) == 0:
                com_square = choice(list_of_not_full)
            else:
                com_square = choice(list_of_signed)
        else:
            com_square = choice(list_of_signed_two_times)
        computer_maxes = check(board, com_square, self)
        list_of_index_to_move = []
        computer_best = max(computer_maxes)
        while True:
            for index, sequence in enumerate(computer_maxes):
                if sequence == computer_best:
                    list_of_index_to_move.append(index)
            while list_of_index_to_move:
                x = choice(list_of_index_to_move)
                y = answers[x]
                com_field = choice(y)
                if not check_if_not_filled(board, com_square, com_field) and com_field in y:
                    y.remove(com_field)
                    if len(y) == 0:
                        list_of_index_to_move.remove(x)
                else:
                    break
            if check_if_not_filled(board, com_square, com_field):
                return com_square, com_field
            # else:
            #     if len(list_of_index_to_move) > 0:
            #         for e in moves[com_field]:
            #             if e in list_of_index_to_move:
            #                 list_of_index_to_move.remove(e)
            #         if len(list_of_index_to_move) == 0:
            #             computer_best -= 1
            #     else:
            computer_best -= 1

    # def defense(self, square, field, board, player):

    #     com_square = square
    #     if len(self.player_moves[square]) == 1:
    #         if field == 4:
    #             com_field = choice([0, 2, 6, 8])
    #         else:
    #             com_field = 4
    #     elif len(self.player_moves[square]) == 2:
    #         if 4 in self.player_moves[square]:
    #             com_field = 8 - field
    #         else:
    #             com_field = choice([3, 5])
    #     elif len(self.player_moves[square]) == 3:
    #         if 4 in self.player_moves[square]:
    #             com_field = 8 - field
    #     elif len(self.player_moves[square]) == 4:
    #         if 4 in self.player_moves[square]:
    #             com_field = 8 - field
    #     self.moves.append(com_field)
    #     return com_square, com_field
