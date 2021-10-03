"""
  N-Queens II
Solution
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
Example:
Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""



class Solution(object):


    def is_not_under_attack(self, board, r, c):
        return board[r][c] == 0

    def printBoard(self, board):
        for i in range(len(board)):
            print board[i]


    def place_queen(self, board, r, c):
        n = len(board)
        print "pre-place, r %d c %d"%(r,c)
        self.printBoard(board)
        print "r=%d,c=%d"%(r,c)


        direc=[(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

        for d in direc:
            newr,newc=r+d[0],c+d[1]

            while  newr<len(board) and newr>=0  and \
                newc<len(board) and newc>=0:

                board[newr][newc]+=1
                newr,newc=newr+d[0],newc+d[1]


        board[r][c] += 1

        self.printBoard(board)
        print "post-place, r %d c %d"%(r,c)


    def remove_queen(self, board, r, c):
        n = len(board)
        print "pre-remove, r %d c %d"%(r,c)
        self.printBoard(board)

        print "r=%d,c=%d"%(r,c)
        direc=[(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

        for d in direc:
            newr,newc=r+d[0],c+d[1]

            while  newr<len(board) and newr>=0  and \
                newc<len(board) and newc>=0:

                board[newr][newc]-=1
                newr,newc=newr+d[0],newc+d[1]


        board[r][c] -= 1
        print "post-remove, r %d c %d"%(r,c)
        self.printBoard(board)

    def queensHelper(self, board, r, num_solutions):

        n = len(board)

        for c in range(n):
            if self.is_not_under_attack(board, r, c):
                self.place_queen(board, r, c)

                if r + 1 == n: #zero based(r) to one based(n)
                    num_solutions[0] += 1
                else:
                    self.queensHelper(board, r+1, num_solutions)

                #backtrack
                self.remove_queen(board, r, c)


    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        #for pass by reference
        num_solutions = [0]
        #attack refcount
        board = [[0] * n for i in range(n)]


        self.queensHelper(board, 0, num_solutions)

        return num_solutions[0]
