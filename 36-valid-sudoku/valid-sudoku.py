class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n, m = len(board), len(board[0])
        def isValid(i, j):
            for x in range(i + 1, n):
                if board[x][j] != '.' and board[x][j] == board[i][j]:
                    return False
            for y in range(j + 1, m):
                if board[i][y] != '.' and board[i][y] == board[i][j]:
                    return False
            start_row, start_col = 3 * (i // 3), 3 * (j // 3)
            for x in range(start_row, start_row + 3):
                for y in range(start_col, start_col + 3):
                    if x != i and y != j and board[x][y] != '.' and board[x][y] == board[i][j]:
                        return False
            return True

        for i in range(n):
            for j in range(m):
                if not isValid(i, j):
                    return False

        return True
        