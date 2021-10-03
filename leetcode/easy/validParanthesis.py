class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)

        i=0;
        ht = {
             '{':1,
             '(':1,
             '[':1,
             '}':2,
             ')':2,
             ']':2
            }

        cp = {
             '}':'{',
             ')':'(',
             ']':'['
             }

        if(length>=1 and ht[s[0]]==2):
            return False
        bkt = []
        count=0
        while(i<length):
            #open
            if(ht[s[i]] == 1):
                bkt.append(s[i])
                count = count + 1
            if(ht[s[i]] == 2):
                if len(bkt)>=1:
                    if(cp[s[i]] != bkt.pop()):
                        return False
                count = count - 1
            i = i + 1

        if count!=0:
            return False
        else:
            return True
