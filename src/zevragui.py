from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from gamemodule import GameView

class ZevraGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.game = GameView(self, 50)

        self.initUI()

    def initUI(self):
        #self.centralwidget = QWidget(self)
        #self.setCentralWidget(self.centralwidget)
        
        self.setWindowTitle('Zevra GUI')
        self.resize(1280, 720)

        self.setCentralWidget(self.game)

        #layout = QVBoxLayout(self.centralWidget())
        
        #layout.addWidget(self.game)

        self.game.setFocus()

        self.show()