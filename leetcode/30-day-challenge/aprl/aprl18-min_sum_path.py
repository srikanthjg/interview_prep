"""
Given a m x n grid filled with non-negative numbers, find a path from
top left to bottom right which minimizes the sum of all numbers
along its path.
Note: You can only move either down or right at any point in time.

"""
##SOLUTION TIME EXCEaEDED
class Solution(object):

    def minPathSumHelper(self,grid,i,j,maxi,maxj,sum):
        print i,j,sum
        ##Base condition
        if i==maxi and j==maxj:
            return sum+grid[i][j]

        ##go right only
        if i==maxi and j<maxj:
            sum=sum+grid[i][j]
            return self.minPathSumHelper(grid,i,j+1,maxi,maxj,sum)
        ##go bottom only
        if i<maxi and j==maxj:
            sum=sum+grid[i][j]
            return self.minPathSumHelper(grid,i+1,j,maxi,maxj,sum)
        ## min(right and bottom)
        if i<maxi and j<maxj:
            sum=sum+grid[i][j]
            return min(self.minPathSumHelper(grid,i+1,j,maxi,maxj,sum),\
            self.minPathSumHelper(grid,i,j+1,maxi,maxj,sum))


    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if len(grid)==0:
            return 0
        maxi=len(grid)-1
        maxj=len(grid[0])-1

        return self.minPathSumHelper(grid,0,0,maxi,maxj,0)




a=[
  [1,3,1],
  [1,0,1],
  [0,2,1]
]

sol=Solution()
print a
print sol.minPathSum(a)
