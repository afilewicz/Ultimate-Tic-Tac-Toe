from constants import DIMENSION


class Single_Board():
    """
    Represents a Single Tic Tac Toe Board.
    """
    def __init__(self):
        self._areas = []
        for i in range(DIMENSION**2):
            self._areas.append(' ')

    @property
    def areas(self):
        return self._areas

    def set(self, field, sign):
        """
        Puts the player sign into given field.
        """
        self.areas[field] = sign

    def filled(self, field):
        """
        Checks if given field is filled.
        """
        return (not self.areas[field] == ' ')

    def full(self):
        """
        Checks if board is full.
        """
        for field in self.areas:
            if field == " ":
                return False
        return True

    def check_how_many_in_sequence(self, person):
        """
        Returns list of player signs in all sequences in given order:
        rows, columns and diagonals.
        """
        columns = []
        rows = []
        diagonals = [0, 0]
        for i in range(DIMENSION):
            columns.append(0)
            rows.append(0)
        for i, field in enumerate(self.areas):
            if field == person.sign:
                for number in range(DIMENSION):
                    if i % DIMENSION == number:
                        columns[number] += 1
                    if i // DIMENSION == number:
                        rows[number] += 1
                if i % (DIMENSION+1) == 0:
                    diagonals[0] += 1
                if (i % DIMENSION + i // DIMENSION) == (DIMENSION-1):
                    diagonals[1] += 1
        any = columns + rows + diagonals
        return any

    def checking_if_win_square(self, person):
        """
        Checks if square has been already won.
        """
        any_max = self.search_max_list(person)[1]
        return (any_max == DIMENSION)

    def search_max_list(self, person):
        """
        Searching for the maxes from the list of "how many in sequence",
        returns sequences which has the most signs and max value of signs
        in sequence.
        """
        any = self.check_how_many_in_sequence(person)
        max_list = []
        max_ = max(any)
        for index, element in enumerate(any):
            if element == max_:
                max_list.append(index)
        return max_list, max_

    def check_which_better(self, player, computer):
        """
        Checks which move is better (offensive or defensive).
        Returns true if offensive and false if defensive.
        When player has 2 sequences in one square to win it attacks.
        """
        if self.checking_if_win_square(player) or\
                self.checking_if_win_square(computer):
            return False
        else:
            can_cover = 0
            have_to_cover = False
            any_player = self.check_how_many_in_sequence(player)
            any_computer = self.check_how_many_in_sequence(computer)
            for index, sequence in enumerate(any_computer):
                if sequence == DIMENSION-1 and any_player[index] == 0:
                    return False
                if any_player[index] == DIMENSION-1 and sequence == 0:
                    have_to_cover = True
                    can_cover += 1
                    if can_cover == 2:
                        return False
            if have_to_cover:
                return True
            return False


class BigBoard():
    """
    Represents Board composed of Single Board.
    Has a representation in SingleBoard class.
    """
    WIDTH_BOARD = 6*DIMENSION**2 + DIMENSION - 2

    def __init__(self):
        self._areas = []
        for i in range(DIMENSION**2):
            self._areas.append(Single_Board())
        self.as_a_small = Single_Board()

    def check_if_winned(self, square):
        """
        Checks if square had been won.
        """
        return (self.as_a_small.areas[square] != ' ')

    def draw_board(self):
        """
        Draws the picture of big board.
        """
        for row in range(DIMENSION**2):
            if row % DIMENSION == 0:
                print(' '+'▬'*self.WIDTH_BOARD)
            else:
                print(' '+'-'*self.WIDTH_BOARD)
            for column in range(DIMENSION**2):
                square_num = (row//DIMENSION)*DIMENSION+column//DIMENSION
                mini_square_num = (row % DIMENSION) * \
                    DIMENSION + column % DIMENSION
                if column % DIMENSION == 0:
                    a = '█'
                else:
                    a = '|'
                print(' '+a, end='  ')
                print(self._areas[square_num].areas[mini_square_num], end=' ')
            print(' █')
        print(' '+'▬'*self.WIDTH_BOARD)

    @property
    def areas(self):
        return self._areas
