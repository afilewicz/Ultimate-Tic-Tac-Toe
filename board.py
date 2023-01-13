from pojedyncza_plansza import dimension

len_single = 19
width_board = 6*dimension**2 + dimension


class Sign:
    def __init__(self):
        self._field = ' '

    def field(self):
        return self._field


class Board:
    def __init__(self):
        self._areas = []
        for field in range(dimension**2):
            element = ' '
            self._areas.append(element)


class Single_Board:
    def __init__(self):
        self._field = Sign()
        self._areas = []
        for field in range(dimension**2):
            self._areas.append(element)

    @property
    def areas(self):
        return self._areas


class BigBoard:

    def __init__(self):
        self._field = Single_Board()
        self._areas = []
        for square in range(dimension**2):
            element = Single_Board()
            self._areas.append(element)

    def draw_board(self):
        for row in range(dimension**2):
            if row % dimension == 0 and row != 0:
                print(' '+'-'*width_board)
            print(' '+'-'*width_board)
            for column in range(dimension**2):
                square_num = (row//dimension)*dimension+column//dimension
                mini_square_num = (row % dimension)*dimension + column % dimension
                if column % dimension == 0 and column != 0:
                    a = '|'
                else:
                    a = ''
                print(' |'+a, end='  ')
                print(self._areas[square_num]._areas[mini_square_num], end=' ')
            print(' |')
        print(' '+'-'*width_board)

    @property
    def areas(self):
        return self._areas

    def set(self, square, mini_square_num, sign):
        self._areas[square]._areas[mini_square_num]._field = sign


board = BigBoard()
# board.draw_board()
