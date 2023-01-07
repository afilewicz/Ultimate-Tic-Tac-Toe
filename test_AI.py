from AI import AI


def test_computer_init():
    computer = AI()
    computer.set_sign('X')
    assert computer.sign == 'X'


def test_second_move():
    computer = AI()
    computer.set_sign('X')
