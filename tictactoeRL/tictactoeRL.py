import numpy as np
BOARD_ROWS=3
BOARD_COLS=3
class tictactoe:
    def __init__(self, p1, p2):
            self.board = np.zeros((BOARD_ROWS, BOARD_COLS))
            self.p1 = p1
            self.p2 = p2
            self.isEnd = False
            self.boardHash = None
            # init p1 plays first
            self.playerSymbol = 1

    def getHash(self):
        self.boardHash = str(self.board.reshape(BOARD_COLS * BOARD_ROWS))
        return self.boardHash

    def availablePositions(self):
            positions = []
            for i in range(BOARD_ROWS):
                for j in range(BOARD_COLS):
                    if self.board[i, j] == 0:
                        positions.append((i, j))  # need to be tuple
            return positions


    def updateState(self, position):
        self.board[position] = self.playerSymbol
        # switch to another player
        self.playerSymbol = -1 if self.playerSymbol == 1 else 1

    def winner(self):
            # row
            for i in range(BOARD_ROWS):
                if sum(self.board[i, :]) == 3:
                    self.isEnd = True
                    return 1
                if sum(self.board[i, :]) == -3:
                    self.isEnd = True
                    return -1
            # col
            for i in range(BOARD_COLS):
                if sum(self.board[:, i]) == 3:
                    self.isEnd = True
                    return 1
                if sum(self.board[:, i]) == -3:
                    self.isEnd = True
                    return -1
            # diagonal
            diag_sum1 = sum([self.board[i, i] for i in range(BOARD_COLS)])
            diag_sum2 = sum([self.board[i, BOARD_COLS - i - 1] for i in range(BOARD_COLS)])
            diag_sum = max(abs(diag_sum1), abs(diag_sum2))
            if diag_sum == 3:
                self.isEnd = True
                if diag_sum1 == 3 or diag_sum2 == 3:
                    return 1
                else:
                    return -1

            # tie
            # no available positions
            if len(self.availablePositions()) == 0:
                self.isEnd = True
                return 0
            # not end
            self.isEnd = False
            return None

    # only when game ends
    def giveReward(self):
            result = self.winner()
            # backpropagate reward
            if result == 1:
                self.p1.feedReward(1)
