import sys
from PyQt5.QtWidgets import QApplication

from zevragui import ZevraGUI

import chess.pgn

if __name__ == '__main__':
    #pgn = open('tcec.pgn')

    #game = chess.pgn.read_game(pgn)
    #while game:
     #   print(type(game))
    #    game = chess.pgn.read_game(pgn)

    app = QApplication(sys.argv)
    gui = ZevraGUI()
    sys.exit(app.exec_())
