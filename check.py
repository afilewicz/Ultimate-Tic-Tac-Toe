from board import dimension

# class Checker:
#     def __init__(self):
#         pass

#     def check(self, board, square, person):
#         fields = person.sign
#         board = board.areas[square]
#         columns = []
#         rows = []
#         diagonals = [0, 0]
#         for i in range(dimension):
#             columns.append(0)
#             rows.append(0)
#         for i, field in enumerate(board.areas):
#             if field in fields:
#                 for number in range(dimension):
#                     if i % dimension == number:
#                         columns[number] += 1
#                     if i // dimension == number:
#                         rows[number] += 1
#                 if (i % dimension + i // dimension) == (dimension-1):
#                     diagonals[1] += 1
#                 if i % (dimension+1) == 0:
#                     diagonals[0] += 1
#         any = columns + rows + diagonals
#         return any


def check_if_not_filled(board, square, field):
    if board.areas[square].areas[field] == ' ':
        return True
    else:
        return False


def checking_if_win_square(board, person, square=None):
    if square is not None:
        fields = person.sign
        board = board.areas[square]
    else:
        fields = person.winned_squares
        board = board
    columns = []
    rows = []
    diagonals = [0, 0]
    for i in range(dimension):
        columns.append(0)
        rows.append(0)
    for i, field in enumerate(board.areas):
        if field in fields:
            for number in range(dimension):
                if i % dimension == number:
                    columns[number] += 1
                if i // dimension == number:
                    rows[number] += 1
            if (i % dimension + i // dimension) == (dimension-1):
                diagonals[1] += 1
            if i % (dimension+1) == 0:
                diagonals[0] += 1
    any = columns + rows + diagonals
    for counter in any:
        if counter == dimension:
            return True
    return False


def check_if_not_full(board, square):
    for field in board.areas[square].areas:
        if field == " ":
            return True
    return False


def check_if_not_a_draw(board):
    for square in range(dimension**2):
        if check_if_not_full(board, square):
            return True
    return False


def check(board, square, person):
    # returns list of sequences (rows, columns and diagonals) for outlined square
    fields = person.sign
    board = board.areas[square]
    columns = []
    rows = []
    diagonals = [0, 0]
    for i in range(dimension):
        columns.append(0)
        rows.append(0)
    for i, field in enumerate(board.areas):
        if field in fields:
            for number in range(dimension):
                if i % dimension == number:
                    columns[number] += 1
                if i // dimension == number:
                    rows[number] += 1
            if (i % dimension + i // dimension) == (dimension-1):
                diagonals[1] += 1
            if i % (dimension+1) == 0:
                diagonals[0] += 1
    any = columns + rows + diagonals
    return any


def search_max(board, square, person):
    # returns number of sequence closest to win for player in square
    any = check(board, square, person)
    max_list = []
    max_ = max(any)
    for index, element in enumerate(any):
        if element == max_:
            max_list.append(index)
    return max_list


def check_which_better(board, square, player, computer):
    if checking_if_win_square(board, player, square) or\
            checking_if_win_square(board, computer, square):
        return False
    else:
        have_to_cover = False
        any_player = check(board, square, player)
        any_computer = check(board, square, computer)
        for index, sequence in enumerate(any_computer):
            if sequence == 2 and any_player[index] == 0:
                return False
            if any_player[index] == 2 and sequence == 0:
                have_to_cover = True
        return have_to_cover
