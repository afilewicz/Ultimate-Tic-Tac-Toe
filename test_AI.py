from AI import AI, make_dict_of_answers


def test_computer_init():
    computer = AI()
    computer.set_sign('X')
    assert computer.sign == 'X'


def test_second_move():
    computer = AI()
    computer.set_sign('X')


def test_attack():
    computer = AI()
    computer.set_sign('O')
    board.set(3, 0, 'X')
    board.set(3, 3, 'O')
    board.set(3, 6, 'O')
    board.set(3, 8, 'O')


def test_make_dict_of_answers():
    answers_2 = make_dict_of_answers()
    assert answers_2 == {
        0: [0, 3, 6],
        1: [1, 4, 7],
        2: [2, 5, 8],
        3: [0, 1, 2],
        4: [3, 4, 5],
        5: [6, 7, 8],
        6: [0, 4, 8],
        7: [2, 4, 6]
    }
