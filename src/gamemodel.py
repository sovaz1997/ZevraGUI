import chess.pgn

class GameModel:
    def __init__(self):
        pgn = open('tcec.pgn')

        self.game = chess.pgn.read_game(pgn)
        self.board = self.game.root()

        self.moves = list(self.game.mainline())
        self.currentPosition = 0

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