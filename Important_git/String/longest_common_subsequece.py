class Solution(object):

    def helper(self,s1,s2,i,j,memo):

        if (i,j) in memo:
            return memo[(i,j)]

        if i>=len(s1) or j>=len(s2):
            return 0

        if s1[i]==s2[j]:
             ans= 1+self.helper(s1,s2,i+1,j+1,memo)
        else:
            ans = max(self.helper(s1,s2,i+1,j,memo),\
                      self.helper(s1,s2,i,j+1,memo))
        memo[(i,j)]=ans
        return ans

    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        memo={}
        return self.helper(text1,text2,0,0,memo)
