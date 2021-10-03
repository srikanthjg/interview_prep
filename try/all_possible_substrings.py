
def substrings(word):
    for i in range(len(word)):
        for j in range(i+1,len(word)+1):
            print word[i:j]

#word="abc"
#print substrings(word)

class Solution(object):
    def helper(self,nums,chosen,out):
        #if len(nums)==0:
        #    return
        #if tuple(chosen) in out:
        #    return
        #out.add(tuple(chosen[:]))
        print chosen
        for i in range(len(nums)):
            chosen.append(nums[i])
            self.helper(nums[i+1:],chosen,out)
            chosen.pop()

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        chosen=[]
        out=set()
        self.helper(nums,chosen,out)
        return out
        
s=Solution()
print s.subsets([1,2,3])
