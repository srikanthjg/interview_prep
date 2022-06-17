#https://leetcode.com/submissions/detail/565340687/
class Solution:
    def findlr(self,nums,mid):
        l=mid
        r=mid

        #go right
        while r<len(nums) and nums[l] == nums[r]:
            r+=1
        r-=1

        #go left
        while l>=0 and nums[l] == nums[r]:
            l-=1
        l+=1
        return [l,r]

    def findlr_bs(self,nums,l,r,target):

        return

    def bs(self,nums,l,r,target):
        #print(l,r,nums,target)
        if l>r:
            return [-1,-1]
        mid=(l+r)//2
        if nums[mid]==target:
            #go left most and right most till same
            res=self.findlr_bs(nums,mid,target)
            return res

        elif target < nums[mid]:
            return self.bs(nums,l,mid-1,target)
        else:
            return self.bs(nums,mid+1,r,target)

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.bs(nums,0,len(nums)-1,target)
