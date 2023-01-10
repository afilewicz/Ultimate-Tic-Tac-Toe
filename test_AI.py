from AI import AI


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