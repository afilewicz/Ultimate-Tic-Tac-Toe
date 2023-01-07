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


def checking_if_win_square(board, person, square=None):
    if square != None:
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


def check(board, square, person):
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
    any = check(board, square, person)
    max_list = []
    max_ = max(any)
    for index, element in enumerate(any):
        if element == max_:
            max_list.append(index)
    return max_list


def check_which_better(board, square, player):
    any = check(board, square, player)
    if 2 in any:
        return True
    else:
        return False
