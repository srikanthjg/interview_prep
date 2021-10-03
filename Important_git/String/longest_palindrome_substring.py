"""
expand around center (odd center and even center)
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s)==1 or len(s)==0:
            return s
        if len(s)==2:
            if s[0]==s[1]:
                return s
            else:
                return s[0]

        max_len=float('-inf')
        ans=""
        for i in range(len(s)):

            odd_center=i
            even_center=i,i+1
            #odd case:
            start=odd_center
            end=odd_center
            while(start >=0 and end<=len(s)-1 and s[start]==s[end]):
                start-=1
                end+=1

            #print start,end
            len1=end-start+1
            #print s[start+1:end],
            if max_len<len1:
                ans=s[start+1:end]
                max_len=len1

                
            #even case:
            start=even_center[0]
            end=even_center[1]
            count=0
            if end>=len(s) or start <0:
                continue
            if s[start]!=s[end]:
                continue
            while(start >=0 and end<len(s) and s[start]==s[end]):
                    start-=1
                    end+=1

            len2=end-start+1
            #print s[start+1:end]
            if max_len<len2:
                ans=s[start+1:end]
                max_len=len2


        #print ans
        return ans
