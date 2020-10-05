"""
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3284/


Algorithm:

"""
class Solution(object):
    depth = 0
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        self.depth  = self.depth + 1
        #print "depth=%d"%self.depth,
        if(self.depth==50):
            return False
        if n==1:
            return True

        digits = []
        while(n):
            r=n%10
            digits.append(r)
            n=n//10
        #print digits,
        sum = 0
        for i in digits:
                sum = sum + (i*i)
        #        print "i=%d,sum=%d"%(i,sum),
        #print ""
        if sum == 1:
            return True
        else:
            return self.isHappy(sum)

sol = Solution()
print sol.isHappy(89)
