from player import Player
from random import choice
from constants import dimension


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

    def defense(self, board, square, sequence_number):
        answers_3 = {
            0: [0, 3, 6],
            1: [1, 4, 7],
            2: [2, 5, 8],
            3: [0, 1, 2],
            4: [3, 4, 5],
            5: [6, 7, 8],
            6: [0, 4, 8],
            7: [2, 4, 6]
        }
        com_square = square
        while True:
            field_choice = choice(answers_3[sequence_number])
            if board.areas[com_square].check_if_not_filled(field_choice):
                com_field = field_choice
                return com_square, com_field
            else:
                answers_3[sequence_number].remove(field_choice)

    def choose_square(self, board):
        com_square = None
        list_of_best = {}
        for i in range(dimension):
            list_of_best[dimension-1-i] = []
        list_of_not_full = []
        for index in range(dimension**2):
            if board.check_if_winned(index):
                continue
            else:
                if board.areas[index].check_if_not_full():
                    list_of_not_full.append(index)
                    max_from_square_list = board.areas[index].search_max_list(self)[1]
                    for i in range(dimension):
                        if (dimension-1-i) == max_from_square_list:
                            list_of_best[dimension-1-i].append(index)
        if len(list_of_not_full) == len(list_of_best[0]):
            com_square = self.choose_field_in_square(board.as_a_small)
            return com_square
        for key in list_of_best:
            if len(list_of_best[key]) != 0:
                com_square = choice(list_of_best[key])
                print(com_square)
                return com_square

    def offense(self, board):
        com_square = self.choose_square(board)
        com_field = self.choose_field_in_square(board.areas[com_square])
        return com_square, com_field

    def choose_field_in_square(self, board):
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
        computer_maxes = board.check_how_many_in_sequence(self)
        list_of_index_to_move = []
        computer_best = max(computer_maxes)
        while True:
            for index, sequence in enumerate(computer_maxes):
                if sequence == computer_best:
                    list_of_index_to_move.append(index)
            while list_of_index_to_move:
                choice_from_best_moves = choice(list_of_index_to_move)
                possible_answer = answers[choice_from_best_moves]
                com_field = choice(possible_answer)
                if board.check_if_not_filled(com_field):
                    return com_field
                else:
                    possible_answer.remove(com_field)
                    if len(possible_answer) == 0:
                        list_of_index_to_move.remove(choice_from_best_moves)
            computer_best -= 1
# zgodnie z moją implementacją nawet jeśli gracz ma pewną wygraną w obu miejscach, ale tego nie zauważy\
#  i atakuje w innym kwadracie, to komputer stawia swoj znak w tym kwadracie probując go wygrać
