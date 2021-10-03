"""
https://leetcode.com/problems/perfect-squares/
Given a positive integer n, find the least number of perfect square
 numbers (for example, 1, 4, 9, 16, ...) which sum to n.
"""
class Solution(object):
    def populateSq(self,sq,n):
        i=1
        while(i*i <=n):
            sq.append(i*i)
            i=i+1

    D=9999
    mem={}
    def dfs(self,sq,sum,depth,n):

        #if sum in self.mem and self.mem[sum]!=9999:
        #    return self.mem[sum]
        #print sq,sum,depth
        if sum>n:
            return 9999
        if sum==n:
            #print "FOUND:",
            #print depth,sum
            if depth<self.D:
                self.D=depth

                return depth

#
        for x in sq:

            d=self.dfs(sq,sum+x,depth+1,n)
            #sq.pop(0)


    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        sq=[]
        retNum=0
        self.populateSq(sq,n)
        if n in sq:
            return 1
        sq.reverse()

        for x in sq:
            self.mem[x]=9999

        op=[]
        sum=0
        depth=0
        self.dfs(sq,sum,depth,n)
        print self.mem
        return self.D

sol=Solution()
print sol.numSquares(12)
