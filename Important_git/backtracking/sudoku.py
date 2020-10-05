class Solution(object):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """

    """
    pseudocode::::

    if board is full:
        return

    while empty spot in the board:
        pick a number between 1-9
        if is not present in row, column or sub-box: #isnumvalid
            fill num in that spot #place
            recurse(board)
            remove num from spot #remove
    """
    def isFull(self, board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    return False

        return True

    def isNumValid(self, board, r,c,val):

        for i in range(len(board[r])):
            if board[r][i] == val:
                return False

        for i in range(len(board)):
            if board[i][c] == val:
                return False

        r1 = r//3
        c1 = c//3

        for i in range(3*r1, 3*r1+3):
            for j in range(3*c1, 3*c1 +3):
                if board[i][j] == val:
                    return False

        return True

    def place(self, board, r,c,val):
        board[r][c] = val

    def remove(self, board, r,c,val):
        board[r][c] = "."

    def nextEmptySpot(self, board):

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    return i, j
        return None, None

    solved=False
    def solveSudoku(self, board):
        r,c = self.nextEmptySpot(board)
        if r == None or c == None:
            return
        #print "r=%d,c=%d"%(r,c)

        #valid = False
        for i in range(1, 10):
            if self.isNumValid(board, r, c, str(i)):
                self.place(board, r,c,str(i))
                if r==8 and c==8:
                    self.solved = True
                    print "solved"
                    print board
                self.solveSudoku(board)
                if not self.solved:
                    self.remove(board, r, c,str(i))




s = Solution()
board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(board)
#print board
print s.isNumValid(board, 0, 0, val)
print ""
