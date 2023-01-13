dimension = 3


class Single_Board:
    def __init__(self):
        element = ' '
        self._areas = []
        for field in range(dimension**2):
            self._areas.append(element)

    @property
    def areas(self):
        return self._areas

    # def make_single_board(self):
    #     for x in range(3):
    #         print(' '+'-'*len_single)
    #         self._areas.append([])
    #         for y in range(3):
    #             print(' |', end='  ')
    #             self._areas[x].append(' ')
    #             print(self._areas[x].areas[y], end=' ')
    #         print(' |')
    #     print(' '+'-'*len_single)


# class Board:

#     def __init__(self):
#         self._arr = []

#     def make_board(self):
#         for x in range(3):
#             for y in range(3):
#                 board = Single_Board()
#                 board.make_single_board()

#     @property
#     def arr(self):
#         return self._arr

#     def set(self, row, column, sign):
#         self._arr[column][row] = sign


# board = Board()
# board.make_board()
# board.set(2, 5, 'X')
# board.set(4, 7, 'O')
# board.make_board()
