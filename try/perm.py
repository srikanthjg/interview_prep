class Solution():
    out=[]
    def perm_helper(self,word,chosen,n):
        if len(chosen)==n:
            self.out.append(chosen)
            return chosen


        for i in range(len(word)):

            tmp=word.pop(i)
            #print tmp, word_copy
            ans=self.perm_helper(word, chosen+tmp,n)
            word.insert(i,tmp)


    def permutation(self,word):
        self.perm_helper(list(word),"",len(word))
        return



word="abc"
s=Solution()
s.permutation(word)
print s.out
