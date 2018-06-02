from collections import defaultdict


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = len(board)
        if row == 0:
            return
        col = len(board[0])

        record = defaultdict(lambda: defaultdict(int))

        for r in range(row):
            for c in range(col):
                if board[r][c] == 1:
                    record[r-1][c-1] += 1
                    record[r-1][c] += 1
                    record[r-1][c+1] += 1
                    record[r][c-1] += 1
                    record[r][c+1] += 1
                    record[r+1][c-1] += 1
                    record[r+1][c] += 1
                    record[r+1][c+1] += 1

        for r in range(row):
            for c in range(col):
                if record[r][c] < 2 or record[r][c] > 3:
                    board[r][c] = 0
                elif board[r][c] == 0 and record[r][c] == 3:
                    board[r][c] = 1

        return board

