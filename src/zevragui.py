from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from game import GameView

class ZevraGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.game = GameView(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Zevra GUI')
        self.resize(1280, 720)

        self.setCentralWidget(self.game)
        self.game.setFocus()

        self.show()