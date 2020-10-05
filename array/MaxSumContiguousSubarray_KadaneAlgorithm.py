"""
Kadane's Algorithm
"""
class Solution(object):

    def maxSum(self,arr):

        cur=0
        best=float("-inf")
        for x in arr:
            cur=cur+x
            best=max(best,cur)
            cur=max(cur,0)  #### for negative numbers
        return best


arr=[5,-3,5,5,-3]
sol=Solution()
print sol.maxSum(arr)
