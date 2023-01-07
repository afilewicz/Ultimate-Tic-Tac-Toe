from computer import Computer
from random import choice
from board import dimension


class AI(Computer):
    def defense(self, square, field, board, player):
        # moves = {
        # 0: ['column_0', 'row_0', 'diagonal_1'],
        # 1: ['column_1', 'row_0'],
        # 2: ['column_2', 'row_0', 'diagonal_2'],
        # 3: ['column_0', 'row_1'],
        # 4: ['column_1', 'row_1', 'diagonal_1', 'diagonal_2'],
        # 5: ['column_2', 'row_1'],
        # 6: ['column_0', 'row_2', 'diagonal_2'],
        # 7: ['column_1', 'row_2'],
        # 8: ['column_2', 'row_2', 'diagonal_1']
        # }
        # answers = {
        # 'column_0': [0, 3, 6],
        # 'column_1': [1, 4, 7],
        # 'column_2': [2, 5, 8],
        # 'row_0': [0, 1, 2],
        # 'row_1': [3, 4, 5],
        # 'row_2': [6, 7, 8],
        # 'diagonal_1': [0, 4, 8],
        # 'diagonal_2': [2, 4, 6]
        # }
        self.player_moves = []
        self.player_moves = []
        for i in range(dimension**2):
            self.player_moves.append([])
            self.moves.append([])
        self.player_moves[square].append([field])
        com_square = square
        if len(self.player_moves[square]) == 1:
            if field == 4:
                com_field = choice([0, 2, 6, 8])
            else:
                com_field = 4
        elif len(self.player_moves[square]) == 2:
            if 4 in self.player_moves[square]:
                com_field = 8 - field
            else:
                com_field = choice([3, 5])
        elif len(self.player_moves[square]) == 3:
            if 4 in self.player_moves[square]:
                com_field = 8 - field
        elif len(self.player_moves[square]) == 4:
            if 4 in self.player_moves[square]:
                com_field = 8 - field
        self.moves.append(com_field)
        return com_square, com_field
