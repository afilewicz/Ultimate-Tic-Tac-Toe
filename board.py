from constants import dimension

len_single = 19
width_board = 6*dimension**2 + dimension


class Board:
    @property
    def areas(self):
        return self._areas


class Single_Board(Board):

    def __init__(self):
        self._areas = []
        for i in range(dimension**2):
            self._areas.append(' ')

    def set(self, square, sign):
        self._areas[square] = sign

    def check_if_not_filled(self, field):
        if self.areas[field] == ' ':
            return True
        else:
            return False

    def check_if_not_full(self):
        for field in self.areas:
            if field == " ":
                return True
        return False

    def check(self, person):
        # returns list of sequences (rows, columns and diagonals) for outlined square
        columns = []
        rows = []
        diagonals = [0, 0]
        for i in range(dimension):
            columns.append(0)
            rows.append(0)
        for i, field in enumerate(self.areas):
            if field == person.sign:
                for number in range(dimension):
                    if i % dimension == number:
                        columns[number] += 1
                    if i // dimension == number:
                        rows[number] += 1
                if i % (dimension+1) == 0:
                    diagonals[0] += 1
                if (i % dimension + i // dimension) == (dimension-1):
                    diagonals[1] += 1
        any = columns + rows + diagonals
        return any

    def checking_if_win_square(self, person):
        any = self.check(person)
        for counter in any:
            if counter == dimension:
                return True
        return False

    def search_max(self, person):
        # returns number of sequence closest to win for player in square
        any = self.check(person)
        max_list = []
        max_ = max(any)
        for index, element in enumerate(any):
            if element == max_:
                max_list.append(index)
        return max_list

    def check_which_better(self, player, computer):
        if self.checking_if_win_square(player) or\
                self.checking_if_win_square(computer):
            return False
        else:
            have_to_cover = False
            any_player = self.check(player)
            any_computer = self.check(computer)
            for index, sequence in enumerate(any_computer):
                if sequence == 2 and any_player[index] == 0:
                    return False
                if any_player[index] == 2 and sequence == 0:
                    have_to_cover = True
            return have_to_cover


class BigBoard(Board):

    def __init__(self):
        self._areas = []
        for i in range(dimension**2):
            self._areas.append(Single_Board())
        self.as_a_small = Single_Board()

    def check_if_winned(self, square):
        if self.as_a_small.areas[square] != ' ':
            return True
        else:
            return False

    def draw_board(self):
        for row in range(dimension**2):
            if row % dimension == 0 and row != 0:
                print(' '+'-'*width_board)
            print(' '+'-'*width_board)
            for column in range(dimension**2):
                square_num = (row//dimension)*dimension+column//dimension
                mini_square_num = (row % dimension) * \
                    dimension + column % dimension
                if column % dimension == 0 and column != 0:
                    a = '|'
                else:
                    a = ''
                print(' |'+a, end='  ')
                print(self._areas[square_num].areas[mini_square_num], end=' ')
            print(' |')
        print(' '+'-'*width_board)

    @property
    def areas(self):
        return self._areas
