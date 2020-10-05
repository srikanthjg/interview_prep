class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j=0

        for i in range(len(nums)):
            if nums[i] ==0 :
                continue;
            else:
                nums[j] = nums[i]
                j = j +1

        #print nums
        while(j<len(nums)):
            #print j
            nums[j]=0
            j = j+1
        return nums

arr=[0,4,1,0,0,3,7]
sol = Solution()
print sol.moveZeroes(arr)
