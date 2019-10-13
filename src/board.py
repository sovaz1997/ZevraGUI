from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtSvg

import chess

class Board(QWidget):
    def __init__(self, cellSize):
        super().__init__()

        self.board = chess.Board()
        self.cellSize = cellSize

        self.pieceImages = [
            [
                QtSvg.QSvgRenderer('images/bP.svg'),
                QtSvg.QSvgRenderer('images/bN.svg'),
                QtSvg.QSvgRenderer('images/bB.svg'),
                QtSvg.QSvgRenderer('images/bR.svg'),
                QtSvg.QSvgRenderer('images/bQ.svg'),
                QtSvg.QSvgRenderer('images/bK.svg'),
            ],
            [
                QtSvg.QSvgRenderer('images/wP.svg'),
                QtSvg.QSvgRenderer('images/wN.svg'),
                QtSvg.QSvgRenderer('images/wB.svg'),
                QtSvg.QSvgRenderer('images/wR.svg'),
                QtSvg.QSvgRenderer('images/wQ.svg'),
                QtSvg.QSvgRenderer('images/wK.svg'),
            ]
        ]

        self.initUI()
    
    def initUI(self):
        print(self.board)
    
    def paintEvent(self, e):
        qp = QPainter();
        qp.begin(self)

        whiteCell = QColor(240, 217, 181)
        blackCell = QColor(181, 136, 99)

        qp.setPen(Qt.NoPen)

        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    qp.setBrush(blackCell)
                else:
                    qp.setBrush(whiteCell)
                
                y, x, w, h = i * self.cellSize, j * self.cellSize, self.cellSize, self.cellSize
                qp.drawRect(x, y, w, h)

                piece = self.board.piece_at(chess.square(j, 7 - i))
                if piece:
                    bounds = QRectF(x, y, w, h)
                    img = self.pieceImages[piece.color][piece.piece_type - 1]
                    img.render(qp, bounds)
                   # img.setGeometry(x, y, w, h)
                    #img.show()


        qp.end()
