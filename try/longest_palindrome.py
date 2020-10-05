class Solution(object):

    def isPalindrome(self,s):
        return s==s[::-1]

    def longestPalindromeBrute(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Brute
        """
        Find all possible substrings
        find if longestPalindrome
        """
        substrings=[]
        best_s=""
        for i in range(len(s)):
            for j in range(i,len(s),1):
                substrings.append(s[i:j+1])
                if self.isPalindrome(s[i:j+1]):
                    if len(best_s)<len(s[i:j+1]):
                        best_s=s[i:j+1]

        print best_s
        print substrings

sol=Solution()
sol.longestPalindromeBrute("abbac")
