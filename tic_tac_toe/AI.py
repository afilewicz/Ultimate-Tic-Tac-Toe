from player import Player
from random import choice
from constants import DIMENSION


def make_dict_of_answers():
    """
    Makes the dictionary of possible answers against the player's move.
    """
    answers = {}
    for i in range(DIMENSION*2 + 2):
        answers[i] = []

    for i in range(DIMENSION**2):
        for number in range(DIMENSION):
            if i % DIMENSION == number:
                answers[number].append(i)
            if i // DIMENSION == number:
                answers[number + DIMENSION].append(i)
        if i % (DIMENSION+1) == 0:
            answers[2*DIMENSION].append(i)
        if (i % DIMENSION + i // DIMENSION) == (DIMENSION-1):
            answers[1 + 2*DIMENSION].append(i)
    return answers


class AI(Player):
    """
    Makes an instance of computer that makes "intelligent" moves.
    """
    def __init__(self):
        super().__init__(name='komputer')

    def defense(self, board, square, player):
        """
        Returns the defensive move. It requires player's last move.
        """
        answers_defense = make_dict_of_answers()
        com_square = square
        any_player = board.areas[square].check_how_many_in_sequence(player)
        any_computer = board.areas[square].check_how_many_in_sequence(self)
        for index, sequence in enumerate(any_computer):
            if any_player[index] == DIMENSION-1 and sequence == 0:
                sequence_number = index
        while True:
            field_choice = choice(answers_defense[sequence_number])
            if not board.areas[com_square].filled(field_choice):
                com_field = field_choice
                return com_square, com_field
            else:
                answers_defense[sequence_number].remove(field_choice)

    def choose_square(self, board):
        """
        Looking for square which has the most signs.
        """
        com_square = None
        list_of_best = {}
        for i in range(DIMENSION):
            list_of_best[DIMENSION-1-i] = []
        list_of_not_full = []
        for index in range(DIMENSION**2):
            if board.check_if_winned(index):
                continue
            else:
                if not board.areas[index].full():
                    list_of_not_full.append(index)
                    sngl_board = board.areas[index]
                    max_from_square_list = sngl_board.search_max_list(self)[1]
                    for i in range(DIMENSION):
                        if (DIMENSION-1-i) == max_from_square_list:
                            list_of_best[DIMENSION-1-i].append(index)
        if len(list_of_not_full) == len(list_of_best[0]):
            com_square = self.choose_field_in_square(board.as_a_small)
            return com_square
        for key in list_of_best:
            if len(list_of_best[key]) != 0:
                com_square = choice(list_of_best[key])
                return com_square

    def offense(self, board):
        """
        Returns computer offensive move.
        """
        com_square = self.choose_square(board)
        com_field = self.choose_field_in_square(board.areas[com_square])
        return com_square, com_field

    def choose_field_in_square(self, board):
        """
        Returns one of the best field to move in given single board.
        """
        answers_offense = make_dict_of_answers()
        computer_maxes = board.check_how_many_in_sequence(self)
        list_of_index_to_move = []
        computer_best = max(computer_maxes)
        while True:
            for index, sequence in enumerate(computer_maxes):
                if sequence == computer_best:
                    list_of_index_to_move.append(index)
            while list_of_index_to_move:
                choice_from_best_moves = choice(list_of_index_to_move)
                possible_answer = answers_offense[choice_from_best_moves]
                com_field = choice(possible_answer)
                if not board.filled(com_field):
                    return com_field
                else:
                    possible_answer.remove(com_field)
                    if len(possible_answer) == 0:
                        list_of_index_to_move.remove(choice_from_best_moves)
            computer_best -= 1
