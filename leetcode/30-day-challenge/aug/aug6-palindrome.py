class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        length=len(s)
        for i in range(length):
            if not s[i].isalnum():
                s = s.replace(s[i]," ")
                continue
            #s = s.split()

        s=s.split()
        s="".join(s)

        length=len(s)
        if length%2==0:
            s1=s[0:length//2]
            s2=s[length//2:]
        else:
            s1=s[0:length//2]
            s2=s[(length+1)//2:]

        print s1,s2

        return s1 == s2[::-1]





s=Solution()
string="A man, a plan, a canal: Panama"
print s.isPalindrome(string)
