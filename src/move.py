from chess.pgn import GameNode

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
        '''
        d - depth
        sd - seldepth
        mt - move time
        tl - total time
        s - speed
        n - nodes
        pv - pv
        h - hash
        wv - white eval
        '''

        comment = multipleSplit(comment, [', ', '='])
        print(comment)

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
            elif comment[i] == 'h':
                self.hashFill = float(comment[i + 1])
            elif comment[i] == 'sd':
                self.selDepth = float(comment[i + 1])
            
        print(self.move, self.color)