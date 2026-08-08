class Solution:
    def gameOfLife(self, board):
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):

                live = 0

                for x in range(max(0, i - 1), min(rows, i + 2)):
                    for y in range(max(0, j - 1), min(cols, j + 2)):
                        if (x != i or y != j) and abs(board[x][y]) == 1:
                            live += 1

                if board[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = -1

                else:
                    if live == 3:
                        board[i][j] = 2

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1