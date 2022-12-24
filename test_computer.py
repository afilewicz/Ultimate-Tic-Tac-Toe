from computer import Computer


def test_init_computer():
    computer = Computer('O')
    assert computer.sign == 'O'
