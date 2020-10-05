class Solution(object):
    #def __init__(self):

    output=[]
    def generateParanthesisHelper(self,n,combo):
        #print combo

        if len(combo)==(2*n):
            self.output.append(combo)
            return


        self.generateParanthesisHelper(n,"("+combo+")")
        self.generateParanthesisHelper(n,"("+")"+combo)
        self.generateParanthesisHelper(n,combo+"("+")")


    def generateParanthesis(self,n):
            self.generateParanthesisHelper(n,"")
            return

    def generateParenthesis_leet(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

    def backtrack(self,string,left,right,length):
        if len(string)==2*length:
            return string

        if left<length:
            return self.backtrack("("+string,left+1,right,length)
        if right<left:
            return self.backtrack(string+")",left,right+1,length)

sol = Solution()
#print sol.generateParenthesis_leet(3)
#print sol.output
print sol.backtrack("", 0, 0,5)

"""
Leet code solution
class Solution1(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans
"""
