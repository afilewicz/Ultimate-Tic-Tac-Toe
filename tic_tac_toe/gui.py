from PySide2.QtWidgets import QApplication, QWidget, QLineEdit
from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout
from PySide2.QtWidgets import QPushButton, QSpinBox, QMainWindow
from PySide2.QtCore import QUrl
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import QRect, QCoreApplication
import sys
from ui_tictactoe import Ui_MainWindow

from game import Game
from board import BigBoard
from player import Player
#from sign import Sign
from AI import AI
from computer import Computer


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
        button.setStyleSheet(u"background-image: url(X.png)")
        button.setEnabled(False)
        square, field = self.game.computer_move()
        row = (square // 3) * 3 + field // 3
        column = (square % 3) * 3 + field % 3
        com_button = self.buttons[row*9+column]
        com_button.setStyleSheet(u"background-image: url(O.png)")
        com_button.setEnabled(False)

    def createButtons(self):
        for row in range(9):
            for column in range(9):
                button = QPushButton(self.ui.centralwidget)
                button.setObjectName(f"pushButton_{row*9+column}")
                button.setGeometry(QRect(38+column*54+2*(column//3), 28+row*54+2*(row//3), 51, 51))
                # button.setText(QCoreApplication.translate("MainWindow", f"{row*9+column}", None))
                button.setStyleSheet("background-color: rgba(184, 234, 239, 1)")
                button.setStyleSheet("border-style: none")
                self.buttons[row*9+column] = button
                self.setup_button(button)


def guiMain(args):
    app = QApplication(args)
    game = Game(Player("name"), Computer(), 'X')
    window = TictactoeWindow(game)
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
