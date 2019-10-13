from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

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

        whiteCell = QColor(240, 217, 181)
        blackCell = QColor(181, 136, 99)

        qp.setPen(QColor(0, 0, 0, 0))
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    qp.setBrush(blackCell)
                else:
                    qp.setBrush(whiteCell)

                qp.drawRect(i * cellSize, j * cellSize, cellSize, cellSize)
        qp.end()
