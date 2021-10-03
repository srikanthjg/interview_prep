#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_map={}
        i=0
        j=0
        ans=0
        n=len(s)
        while(i<n and j<n):
            if s[j] not in hash_map:
                hash_map[s[j]]=True
                ans=max(ans,j-i+1)
                j+=1
            else:
                del hash_map[s[i]]
                i+=1
        return ans
