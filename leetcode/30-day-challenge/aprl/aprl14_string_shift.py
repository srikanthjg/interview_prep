"""
string and list operations are different
so convert string to list before any string assignement operations



"""
class Solution(object):
    def rotateRight(self,string):
        string=list(string)
        tmp=string[-1]
        for i in range(len(string)-1,0,-1):
            string[i]=string[i-1]

        string[0]=tmp
        return ''.join(string)

    def rotateLeft(self,string):
        string=list(string)
        tmp=string[0]
        for i in range(1,len(string)):
            string[i-1]=string[i]
        string[-1]=tmp

        return ''.join(string)

    def rotateString(self,string,rot):
        if rot>0:
            for i in range(rot):
                string=self.rotateRight(string)
        elif(rot<0):
            for i in range(abs(rot)):
                string=self.rotateLeft(string)
        else:
            return string

        return string

    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        #shift[i] = [direction, amount]:

        #calc rotation
        rot=0
        for i in range(len(shift)):
            if shift[i][0]==0:
                shift[i][1]=-shift[i][1]
            rot=rot+shift[i][1]

        print rot
        string = self.rotateString(s,rot)

        return string

s = "wpdhhcj"
shift=[[0,7],[1,7],[1,0],[1,3],[0,3],[0,6],[1,2]]
sol=Solution()
print sol.stringShift(s,shift)
