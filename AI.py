from player import Player
from random import choice, randint
from board import dimension


def make_dict_of_answers():
    answers_2 = {}
    for i in range(dimension*2 + 2):
        answers_2[i] = []

    for i in range(dimension**2):
        for number in range(dimension):
            if i % dimension == number:
                answers_2[number].append(i)
            if i // dimension == number:
                answers_2[number + dimension].append(i)
        if i % (dimension+1) == 0:
            answers_2[2*dimension].append(i)
        if (i % dimension + i // dimension) == (dimension-1):
            answers_2[1 + 2*dimension].append(i)
    return answers_2


answers_2 = make_dict_of_answers()
# answers_2 = {
#     0: [0, 3, 6],
#     1: [1, 4, 7],
#     2: [2, 5, 8],
#     3: [0, 1, 2],
#     4: [3, 4, 5],
#     5: [6, 7, 8],
#     6: [0, 4, 8],
#     7: [2, 4, 6]
# }

# moves = {
#     0: [0, 3, 6],
#     1: [1, 3],
#     2: [2, 3, 7],
#     3: [0, 4],
#     4: [1, 4, 6, 7],
#     5: [2, 4],
#     6: [0, 5, 7],
#     7: [1, 5],
#     8: [2, 5, 6]
# }


class AI(Player):
    def __init__(self):
        super().__init__(name='computer')
        self.player_moves = []
        self.moves = []
        for square in range(dimension**2):
            self.player_moves.append([])
            self.moves.append([])
            for field in range(dimension**2):
                self.player_moves[square].append([])

    def defense(self, board, square, player):
        # if board.areas[square].checking_if_win_square(player) or\
        #         board.areas[square].checking_if_win_square(self):
        #     com_square = randint(0, dimension**2)
        # else:
        com_square = square
        player_max = board.areas[square].search_max(player)
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
            if board.areas[index].checking_if_win_square(player) or\
                    board.areas[index].checking_if_win_square(self):
                continue
            else:
                if board.areas[index].check_if_not_full():
                    max_from_square_list = board.areas[index].search_max(self)
                    list_of_not_full.append(index)
                    # czy mozna zrobic tak ze nie odroznia gdy jest 1 lub 2 w danym kwadracie
                    if len(max_from_square_list) <= 4 and 4 in max_from_square_list:
                        list_of_signed.append(index)
                    elif len(max_from_square_list) < (2*dimension+1):
                        list_of_signed_two_times.append(index)
        if len(list_of_signed_two_times) == 0:
            if len(list_of_signed) == 0:
                com_square = choice(list_of_not_full)
            else:
                com_square = choice(list_of_signed)
        else:
            com_square = choice(list_of_signed_two_times)

        computer_maxes = board.areas[com_square].check(self)
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
                if not board.areas[com_square].check_if_not_filled(com_field) and com_field in y:
                    y.remove(com_field)
                    if len(y) == 0:
                        list_of_index_to_move.remove(x)
                else:
                    break
            if board.areas[com_square].check_if_not_filled(com_field):
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
