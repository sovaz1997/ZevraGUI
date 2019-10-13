from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from board import Board

class ZevraGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.board = Board(50)

        self.initUI()

    def initUI(self):
        widget = QWidget(self)
        self.setCentralWidget(widget)

        self.setWindowTitle('Zevra GUI')
        self.resize(1280, 720)

        layout = QVBoxLayout(widget)
        layout.addWidget(self.board)

        self.show()