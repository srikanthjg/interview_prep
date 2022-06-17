class Solution(object):

    def bs(self,nums,s,e,target):
        #print s,e,target

        #Not found!
        if e<s:
            return -1

        mid=(s+e)//2
        if target==nums[mid]:
            return mid
        elif target<nums[mid]:
            return self.bs(nums,s,mid-1,target)
        elif target>nums[mid]:
            return self.bs(nums,mid+1,e,target)


    def findPivot(self,nums,s,e):
        if e<s:
            return -1
        if s==e:
            return s
        mid=(s+e)//2
        if (nums[mid] >nums[mid+1]):
            return mid
        if nums[s]>nums[mid]:
            return self.findPivot(nums,s,mid-1)
        return self.findPivot(nums,mid+1,e)

    #perform bs on a rotated sorted arr
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)-1
        if n+1==0:
            return -1

        pivot = self.findPivot(nums,0,n)
        #print pivot

        if target == nums[pivot]:
            return pivot
        if pivot==-1:
            return self.bs(nums,0,n,target)

        ret = self.bs(nums,0,pivot,target)
        if ret ==-1:
            return self.bs(nums,pivot+1,n,target)
        else:
            return ret
    
