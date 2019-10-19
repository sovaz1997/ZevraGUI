import sys
from PyQt5.QtWidgets import QApplication

from zevragui import ZevraGUI

import chess.pgn

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = ZevraGUI()
    sys.exit(app.exec_())