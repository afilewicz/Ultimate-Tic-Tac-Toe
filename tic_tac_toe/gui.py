from PySide2.QtWidgets import QApplication, QWidget, QLineEdit
from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout
from PySide2.QtWidgets import QPushButton, QSpinBox, QMainWindow
from PySide2.QtCore import Qt, QUrl
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import QRect, QCoreApplication
from PySide2.QtGui import QPainter, QPen, QIcon
import sys
from ui_tictactoe import Ui_MainWindow

from game import Game
from board import BigBoard
from player import Player
#from sign import Sign
from AI import AI
from computer import Computer

from time import sleep


class TictactoeWindow(QMainWindow):
    def __init__(self, game, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.buttons = {}
        self.createButtons()
        self.game = game

    def setup_button(self, button):
        button.clicked.connect(lambda: self.change_sign(button, self.game.player))

    def change_sign(self, button, player):
        sign = 'X.png'
        self.clicked_button(button, sign)
        square = int(button.objectName().split("_")[1])
        field = int(button.objectName().split("_")[2])
        self.game.board.areas[square].set(field, player.sign)
        self.end_round(player, square)
        if (self.game.result is None):
            self.computer_move()

    def computer_move(self):
        sign = 'O.png'
        square, field = self.game.computer_move()
        com_button = self.buttons[square][field]
        if (com_button.isEnabled() is False):
            self.computer_move()
        else:
            self.clicked_button(com_button, sign)
            self.game.board.areas[square].set(field, self.game.computer.sign)
            self.end_round(self.game.computer, square)
        self.game.board.draw_board()

    def end_round(self, player, square):
        if (self.game.check_if_end(square, player)):
            if self.game.result is True:
                print(f"Zwycięzcą został/a {self.game.winner.name}")
            else:
                print("Nie ma zwycięzcy")
            for buttons in self.buttons.values():
                for butto in buttons.values():
                    butto.setEnabled(False)
        if (self.game.board.as_a_small.filled(square)):
            self.disable_buttons_in_square(square, player)

    def clicked_button(self, button, sign):
        button.setStyleSheet(f"background-image: url({sign});"
                     "background-position: center;"
                     "border-style: none;")
        button_geometry = button.geometry()
        x = button_geometry.x()
        y = button_geometry.y()
        button.setGeometry(QRect(x+4, y+2, 44, 44))
        button.setEnabled(False)

    def disable_buttons_in_square(self, square, player):
        if self.game.board.areas[square].checking_if_win_square(player):
            for but in self.buttons[square].values():
                # but.setEnabled(False)
                # pixmap = but.grab()
                # painter = QPainter(pixmap)
                # painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
                # painter.drawLine(0, 0, pixmap.width(), pixmap.height())
                # painter.end()
                # but.setIcon(QIcon(pixmap))
                but.setEnabled(False)

    def createButtons(self):
        for row in range(9):
            for column in range(9):
                button = QPushButton(self.ui.centralwidget)
                square = (row // 3) * 3 + column // 3
                field = (row % 3) * 3 + column % 3
                button.setObjectName(f"pushButton_{square}_{field}")
                button.setGeometry(QRect(38+column*54+2*(column//3), 28+row*54+2*(row//3), 51, 51))
                # button.setText(QCoreApplication.translate("MainWindow", f"{row*9+column}", None))
                button.setStyleSheet("background-color: rgba(184, 234, 239, 1)")
                button.setStyleSheet("border-style: none")
                if (square not in self.buttons.keys()):
                    self.buttons[square] = {}
                self.buttons[square][field] = button
                self.setup_button(button)


def guiMain(args):
    app = QApplication(args)
    game = Game(Player("name"), Computer(), 'X')
    window = TictactoeWindow(game)
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
