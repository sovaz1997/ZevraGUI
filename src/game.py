from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtSvg

import chess.pgn


class GameModel:
    def __init__(self):
        self.pgnSrc = open('tcec.pgn')

        self.game = chess.pgn.read_game(self.pgnSrc)
        self.board = self.game.board()

        self.moves = list(self.game.mainline())
        self.currentPosition = 0
    
    def __del__(self):
        self.pgnSrc.close()

    def goForward(self):
        if self.currentPosition < len(self.moves) - 1:
            self.board.push(self.moves[self.currentPosition].move)
            self.currentPosition += 1
            return True
        return False
    
    def goBack(self):
        if self.currentPosition > 0:
            self.board.pop()
            self.currentPosition -= 1
            return True
        return False

    def getBoard(self):
        return self.board

class GameView(QWidget):
    def __init__(self, parent, cellSize):
        super(QWidget, self).__init__(parent)
        self.controller = GameController(self)

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
        self.show()

    def keyPressEvent(self, e):
        key = e.key()

        if key == Qt.Key_Right:
            self.controller.goForward()
        elif key == Qt.Key_Left:
            self.controller.goBack()
    
    def wheelEvent(self, e):
        if e.angleDelta().y() < 0:
            self.controller.goForward()
        else:
            self.controller.goBack()
    
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

class GameController:
    def __init__(self, view):
        self.view = view
        self.model = GameModel()

    def goForward(self):
        res = self.model.goForward()
        
        if res:
            self.view.update()
    
    def goBack(self):
        res = self.model.goBack()
        
        if res:
            self.view.update()
    
    def getBoardState(self):
        return self.model.getBoard()