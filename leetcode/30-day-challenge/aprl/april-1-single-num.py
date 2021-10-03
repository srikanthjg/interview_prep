
"""
Q:
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3283/
Algorithm:
toggle bit in the number that appears in the arr.
all apprear twice execpt 1.So, only one number will be set

one bitmap for +nums
one bitmap for -nums
"""
class Solution(object):
    def toggleKthBit(self,n, k):
        return (n ^ (1 << (k)))

    def isbitset(self,n,k):
        tmp = 1<<k
        if(tmp & n):
            return True
        else:
            return False

    def single_num(self,arr):
        posnum=0
        negnum=0
        for n in arr:
            #print "n=%d"%n,
            if n >= 0:
                posnum = self.toggleKthBit(posnum,n)
            else:
                negnum = self.toggleKthBit(negnum,abs(n))

#        print "posnum=%d,negnum=%d"%(posnum,negnum)
#        print  ""
    ##check set at each position
        for n in arr:
#            print n,
            if n >=0 :
                if(self.isbitset(posnum,n)):
                    return n
            else:
                if(self.isbitset(negnum,abs(n))):
                    return n

arr=[2,2,-1]
sol = Solution()

print sol.single_num(arr)
