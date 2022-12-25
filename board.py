width_board = 57


class Board:

    def __init__(self):
        self._areas = []
        self.winned_squares_player = []
        self.winned_squares_computer = []

    def make_board(self):
        for x in range(9):
            if x % 3 == 0 and x != 0:
                print(' '+'-'*width_board)
            print(' '+'-'*width_board)
            if x % 3 == 0 and len(self._areas) < 9:
                self._areas.append([])
                self._areas.append([])
                self._areas.append([])
            for y in range(9):
                square_num = (x//3)*3+y//3
                square_column = (x % 3)*3 + y % 3
                if y % 3 == 0 and y != 0:
                    a = '|'
                else:
                    a = ''
                print(' |'+a, end='  ')
                if len(self.areas[square_num]) < 9:
                    self._areas[square_num].append(' ')
                print(self._areas[square_num][square_column], end=' ')
            print(' |')
        print(' '+'-'*width_board)

    @property
    def areas(self):
        return self._areas

    def set(self, square, column, sign):
        self._areas[square][column] = sign


board = Board()
board.make_board()
