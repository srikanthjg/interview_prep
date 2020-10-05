class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        st=0
        r=0
        l=0
        s = sorted(list(s))
        print s
        for i in s:
            #print stack
            if i=="*":
                st=st+1
                continue
            if i=="(":
                l=l+1
                stack.append(i)
                continue
            elif i == ")":
                r=r+1
                if len(stack)!=0 and r>0:
                    stack.pop()
                    continue

        print stack,l,r

        if abs(l-r)<=st:
            return True
        return False

sol= Solution()
s="*("
print sol.checkValidString(s)
