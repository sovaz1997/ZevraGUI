from chess.pgn import GameNode
import defs

def multipleSplit(s, splits):
    for i in splits:
        s = s.replace(i, '|')
    return s.split('|')

class Move:
    def __init__(self, gameNode):
        self.move = gameNode.move
        self.color = not gameNode.board().turn
        self.parse(gameNode.comment)
    
    def parse(self, comment):
        comment = multipleSplit(comment, [', ', '='])

        for i in range(len(comment)):
            if comment[i] == 'd':
                self.depth = int(comment[i + 1])
            elif comment[i] == 'sd':
                self.selDepth = int(comment[i + 1])
            elif comment[i] == 'mt':
                self.moveTime = int(comment[i + 1])
            elif comment[i] == 'tl':
                self.totalTime = int(comment[i + 1])
            elif comment[i] == 's':
                self.speed = int(comment[i + 1])
            elif comment[i] == 'n':
                self.nodesCount = int(comment[i + 1])
            elif comment[i] == 'pv':
                self.pv = comment[i + 1]
            elif comment[i] == 'wv':
                self.eval = float(comment[i + 1])