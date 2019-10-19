from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtSvg

import chess.pgn

class BoardView(QWidget):
    def __init__(self, parent, controller, cellSize):
        super(QWidget, self).__init__(parent)

        self.cellSize = cellSize
        self.controller = controller

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
        self.show()
    
    def paintEvent(self, e):
        qp = QPainter();
        qp.begin(self)

        whiteCell = QColor(240, 217, 181)
        blackCell = QColor(181, 136, 99)

        qp.setPen(Qt.NoPen)


        board = self.controller.getBoardState()

        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    qp.setBrush(blackCell)
                else:
                    qp.setBrush(whiteCell)
                
                y, x, w, h = i * self.cellSize, j * self.cellSize, self.cellSize, self.cellSize
                qp.drawRect(x, y, w, h)

                piece = board.piece_at(chess.square(j, 7 - i))
                if piece:
                    bounds = QRectF(x, y, w, h)
                    img = self.pieceImages[piece.color][piece.piece_type - 1]
                    img.render(qp, bounds)


        qp.end()