class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def isSafe(board, r, c, number):
            for i in range(9):
                if board[r][i] == number:
                    return False

            for i in range(9):
                if board[i][c] == number:
                    return False

            startR = r - r % 3
            startC = c - c % 3

            for i in range(3):
                for j in range(3):
                    if board[startR + i][startC + j] == number:
                        return False
            return True

        def backtracking(r, c):
            if r == 9:
                return True
            if c == 9:
                return backtracking(r + 1, 0)
            if board[r][c] != '.':
                return backtracking(r, c + 1)
            for num in range(1, 10):
                if isSafe(board, r, c, str(num)):
                    board[r][c] = str(num)
                    if backtracking(r, c + 1):
                        return True
                    board[r][c] = '.'
            return False

        backtracking(0, 0)
