from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtSvg

import chess.pgn

from move import Move
from board import BoardView

class GameModel:
    def __init__(self):
        self.pgnSrc = open('tcec.pgn')

        self.game = chess.pgn.read_game(self.pgnSrc)
        self.board = self.game.board()

        self.moves = [Move(i) for i in list(self.game.mainline())]

        self.currentPosition = 0
    
    def __del__(self):
        self.pgnSrc.close()

    def goForward(self):
        if self.currentPosition < len(self.moves) - 1:
            self.board.push(self.getCurrentNode().move)
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
    
    def getCurrentNode(self):
        return self.moves[self.currentPosition]

class GameView(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.controller = GameController(self)
        self.boardView = BoardView(self.controller, 100)

        self.initUI()
    
    def initUI(self):
        layout = QHBoxLayout()
        layout.addWidget(self.boardView)
        self.setLayout(layout)

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