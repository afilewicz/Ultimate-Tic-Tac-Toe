width_board = 57
dimension = 3


class Board:

    def __init__(self):
        self._areas = []
        for row in range(dimension**2):
            if row % 3 == 0:
                self._areas.append([])
                self._areas.append([])
                self._areas.append([])
            for column in range(dimension**2):
                square_num = (row//3)*3+column//3
                self._areas[square_num].append(' ')

    def draw_board(self):
        for row in range(dimension**2):
            if row % 3 == 0 and row != 0:
                print(' '+'-'*width_board)
            print(' '+'-'*width_board)
            for column in range(dimension**2):
                square_num = (row//3)*3+column//3
                mini_square_num = (row % 3)*3 + column % 3
                if column % 3 == 0 and column != 0:
                    a = '|'
                else:
                    a = ''
                print(' |'+a, end='  ')
                print(self._areas[square_num][mini_square_num], end=' ')
            print(' |')
        print(' '+'-'*width_board)

    @property
    def areas(self):
        return self._areas

    def set(self, square, mini_square_num, sign):
        self._areas[square][mini_square_num] = sign
