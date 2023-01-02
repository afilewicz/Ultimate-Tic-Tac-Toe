from computer import Computer


def test_computer_init():
    computer = Computer()
    computer.set_sign('X')
    assert computer.sign == 'X'


# def test_computer_move(monkeypatch):
#     computer = Computer()
#     player = Player('Adam', 'O')
#     game = Game(player, computer)
#     assert game.computer.sign == 'X'

#     def set_place(a, b):
#         return 6, 7
#     monkeypatch.setattr('computer.Computer.move', set_place)
#     assert game.board.areas[6][7] == 'X'
