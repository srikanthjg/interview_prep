class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        #key=(tup(chosen),tup(rest))
        #value=final permutation
        memo={}
        #nums.sort()
        if len(set(nums))<2:
            return [nums]
        res=[]
        self.helper(res,[],nums,memo)
        return res

    def helper(self,res,chosen,nums, memo):
        t=tuple(chosen)
        #print(t)

        if t in memo:
            return memo

        if len(nums)==0:
            out=chosen[:]
            res.append(out)
            memo[t]=out
            return out


        ret=[]
        for i in range(len(nums)):
            a=nums.pop(i)
            chosen.append(a)

            ans=self.helper(res,chosen,nums,memo)
            ret.append(ans)

            chosen.pop()
            nums.insert(i,a)

        memo[t]=ret
        return ret




        
