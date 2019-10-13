from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtSvg

from board import Board

import chess

class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.board = Board(50)
        self.initUI()
    
    def initUI(self):
        layout = QHBoxLayout(self)
        layout.addWidget(self.board)
        self.show()