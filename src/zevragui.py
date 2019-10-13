from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from game import Game

class ZevraGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.game = Game()

        self.initUI()

    def initUI(self):
        #widget = QWidget(self)
        self.setCentralWidget(self.game)

        self.setWindowTitle('Zevra GUI')
        self.resize(1280, 720)

        #layout = QVBoxLayout(widget)
        #layout.addWidget(self.board)

        self.show()