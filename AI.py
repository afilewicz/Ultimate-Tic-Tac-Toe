from computer import Computer
from random import choice, randint
from board import dimension
from check import check, search_max, checking_if_win_square

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
        com_field = choice(answers[choice(player_max)])
        return com_square, com_field

    def offense(self, board, player):
        list_ = []
        choice_from = []
        for index in range(dimension**2):
            if checking_if_win_square(board, player, index) or\
                    checking_if_win_square(board, self, index):
                continue
            else:
                max_list = search_max(board, index, self)
                choice_from.append(index)
                if len(max_list) < (2*dimension-1):
                    list_.append(index)
        if len(list_) == 0:
            com_square = choice(choice_from)
        else:
            com_square = choice(list_)
        computer_max = check(board, com_square, self)
        com_field = choice(answers[choice(computer_max)])
        return com_square, com_field



    # def defense(self, square, field, board, player):
    #     # moves = {
    #     # 0: ['column_0', 'row_0', 'diagonal_1'],
    #     # 1: ['column_1', 'row_0'],
    #     # 2: ['column_2', 'row_0', 'diagonal_2'],
    #     # 3: ['column_0', 'row_1'],
    #     # 4: ['column_1', 'row_1', 'diagonal_1', 'diagonal_2'],
    #     # 5: ['column_2', 'row_1'],
    #     # 6: ['column_0', 'row_2', 'diagonal_2'],
    #     # 7: ['column_1', 'row_2'],
    #     # 8: ['column_2', 'row_2', 'diagonal_1']
    #     # }



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
