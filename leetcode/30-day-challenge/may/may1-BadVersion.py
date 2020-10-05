"""
Get the entire bad list
return 1st with binary search

if true : index=  mid+1,end
else: index = s,mid
"""




# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def helper(self,s,e):
        mid=(s+e)//2
        cur = not isBadVersion(mid)
        #print s,e,mid,cur
        #b4 = isBadVersion(mid-1)
        if s>e:
            return -1
        if s==e and cur==False:
            return mid

        if cur == False:
            return self.helper(s,mid)
        else:
            return self.helper(mid+1,e)
        return -1

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n==0:
            return True

        return self.helper(1,n)

        
