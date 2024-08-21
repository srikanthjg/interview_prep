import math

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        distance = 0
        for i in range(1,len(A)):
            distance = distance + math.floor(math.sqrt((A[i]-A[i-1])**2 + (B[i]-B[i-1])**2))
            #print distance
        return int(distance)

A=[0,1,1]
B=[0,1,2]

sol = Solution()
print sol.coverPoints(A,B)
