#https://leetcode.com/problems/unique-paths
class Solution(object):

    memo={}
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if (m,n) in self.memo:
            return self.memo[(m,n)]

        if m==1 or n==1:
            self.memo[(m,n)]=1
            return 1

        self.memo[(m,n)]= self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)
        return self.memo[(m,n)]


#https://leetcode.com/problems/unique-paths-ii/
class Solution(object):

    def helper(self,obs,m,n,memo):
        if (m,n) in memo:
            return memo[m,n]

        if m<0 or n<0 or m>=len(obs) or n>=len(obs[0]):
            memo[(m,n)]=0
            return 0
        if obs[m][n]==1:
            memo[(m,n)]=0
            return 0
        if obs[m-1][n]==1 and obs[m][n-1]==1:
            memo[(m,n)]=0
            return 0

        if m==0 and n==0:
            memo[(m,n)]=1
            return 1

        u=self.helper(obs,m,n-1,memo)
        l=self.helper(obs,m-1,n,memo)
        if obs[m-1][n]==1 and obs[m][n-1]==0:
            memo[(m,n)]=u
            return u
        elif obs[m-1][n]==0 and obs[m][n]==1:
            memo[(m,n)]=l
            return l
        else:
            memo[(m,n)]=u+l
            return u+l


    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)-1
        n=len(obstacleGrid[0])-1
        start=(0,0)
        end=(m,n)

        memo={}
        return self.helper(obstacleGrid,m,n,memo)
