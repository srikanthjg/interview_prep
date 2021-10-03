"""
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
"""

class Solution(object):
    def pruneList(self,s):
        i=0   # go over all elements in s
        itr=0 # used index elements in pruned list
        length=len(s)

        while(i<length):
            # "#s"
            if(s[itr]=="#" and itr==0):
                s.remove(s[itr])
                #itr will not get updated
                i=i+1
                continue
            # "s#"
            elif(s[itr]=="#"):
                s.remove(s[itr])
                itr=itr-1
                s.pop(itr)
                #itr=itr-1
                i=i+1
                continue
            else:
                itr=itr+1
                i=i+1
        return s

    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        return self.pruneList(list(S)) ==\
               self.pruneList(list(T))

S="y#fo##f"
T="y#f#o##f"
sol = Solution()
#print sol.backspaceCompare(S,T)
print sol.pruneList(list(T))
