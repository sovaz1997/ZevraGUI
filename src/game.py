from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtSvg


from board import Board
import chess.pgn

class Game(QWidget):
    def __init__(self):
        super().__init__()

        pgn = open('tcec.pgn')

        self.game = chess.pgn.read_game(pgn)
        self.board = Board(50)

        self.moves = list(self.game.mainline())
        self.currentPosition = 0

        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout(self)
        layout.addWidget(self.board)
        self.show()

    def openPgn(self):
        self.board.setFen(game.board.fen())

    def goForward(self):
        if self.currentPosition < len(self.moves) - 1:
            self.board.push(self.moves[self.currentPosition].move)
            self.currentPosition += 1
    
    def goBack(self):
        if self.currentPosition > 0:
            self.board.pop()
            self.currentPosition -= 1

    def keyPressEvent(self, e):
        key = e.key()

        if key == Qt.Key_Right:
            self.goForward()
        elif key == Qt.Key_Left:
            self.goBack()
    
    def wheelEvent(self, e):
        if e.angleDelta().y() < 0:
            self.goForward()
        else:
            self.goBack()