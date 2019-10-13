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
        game = chess.pgn.read_game(pgn)

        self.game = game
        self.board = Board(50)

        self.moves = list(self.game.mainline_moves())
        self.currentPosition = 0

        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout(self)
        layout.addWidget(self.board)
        self.show()

    def openPgn(self):
        self.board.setFen(game.board.fen())

    def goForward(self):
        print('>')

        if self.currentPosition < len(self.moves) - 1:
            self.board.push(self.moves[self.currentPosition])
            self.currentPosition += 1
    
    def goBack(self):
        print('>')

        if self.currentPosition > 0:
            self.board.pop()
            self.currentPosition -= 1
