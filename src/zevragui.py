from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from game import Game

class ZevraGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.game = Game()

        self.initUI()

    def initUI(self):
        self.setCentralWidget(self.game)

        self.setWindowTitle('Zevra GUI')
        self.resize(1280, 720)

        self.show()
        
    def keyPressEvent(self, e):
        key = e.key()

        if key == Qt.Key_Right:
            self.game.goForward()
        elif key == Qt.Key_Left:
            self.game.goBack()