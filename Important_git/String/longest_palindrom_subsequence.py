class Solution(object):

    def helper(self,s,l,r,memo):
        if (l,r) in memo:
            return memo[(l,r)]

        if l==r:
            memo[(l,r)]=1
            return 1
        if l>r:
            memo[(l,r)]=0
            return 0


        if s[l]==s[r]:
            ans=2+(self.helper(s,l+1,r-1,memo))
        else:
            ans= max(self.helper(s,l+1,r,memo),\
                     self.helper(s,l,r-1,memo))
        memo[(l,r)]=ans
        return ans




    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo={}
        return self.helper(s,0,len(s)-1,memo)
