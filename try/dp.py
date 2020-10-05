class Solution(object):

    minSum=float('inf')
    def helper(self,cur,grid,end,sum,dp):
        x,y=cur
        print cur
        if dp[x][y] != float('inf'):
            return dp[x][y]
        sum=sum+grid[x][y]

        dir=[(0,1),(1,0)]
        if end==cur:
            self.minSum=min(self.minSum,sum)
            dp[x][y]=self.minSum
            return self.minSum


        for d in dir:
            newx=x+d[0]
            newy=y+d[1]
            cur=(newx,newy)

            if 0<=newx<=len(grid)-1 and \
                0<=newy<=len(grid[0])-1:
                  s= self.helper(cur,grid,end,sum,dp)
                  self.minSum=min(s,self.minSum)

        dp[x][y]=self.minSum
        return dp[x][y]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #down,right
        dp=[ [float('inf') for i in range(len(grid))] for i in range(len(grid[0])) ]
        end=(len(grid)-1,len(grid[0])-1)
        sum=0
        cur=(0,0)
        #print dp
        self.helper(cur,grid,end,sum,dp)
        print self.minSum
        print dp

        return self.minSum

input=[range(1,4) for i in range(3)]
sol=Solution()
print input
print input
print sol.minPathSum(input)
