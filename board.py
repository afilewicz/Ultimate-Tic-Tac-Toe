width_board = 57


class Board:

    def __init__(self):
        self._areas = []

    def make_board(self):
        for x in range(9):
            if x % 3 == 0 and x != 0:
                print(' '+'-'*width_board)
            print(' '+'-'*width_board)
            self._areas.append([])
            for y in range(9):
                if y % 3 == 0 and y != 0:
                    a = '|'
                else:
                    a = ''
                print(' |'+a, end='  ')
                self._areas[x].append(f'{x}, {y}')
                print(self._areas[x][y], end=' ')
            print(' |')
        print(' '+'-'*width_board)

    @property
    def areas(self):
        return self._areas

    def set(self, row, column, sign):
        self._areas[column][row] = sign


board = Board()
board.make_board()
