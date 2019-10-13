from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter

import chess

class Board(QWidget):
    def __init__(self, size):
        super().__init__()

        self.board = chess.Board()
        self.size = size

        self.initUI()
    
    def initUI(self):
        print(self.board)
    
    def paintEvent(self, e):
        qp = QPainter();
        qp.begin(self)
        cellSize = self.size / 8;
        for i in range(8):
            for j in range(8):
                qp.drawRect(i * cellSize, j * cellSize, cellSize, cellSize)
        qp.end()
