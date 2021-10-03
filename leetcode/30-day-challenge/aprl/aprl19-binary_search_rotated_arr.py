"""
Suppose an array sorted in ascending order is rotated at some pivot
 unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index,
otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""
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

# Function to get pivot. For array
# 3, 4, 5, 6, 1, 2 it returns 3
# (index of 6)
## sorted arr will return index of max
#### Find index of max int
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

        pivot = self.findPivota(nums,0,n)
        print pivot

        if target == nums[pivot]:
            return pivot
        if pivot==-1:
            return self.bs(nums,0,n,target)

        ret = self.bs(nums,0,pivot,target)
        if ret ==-1:
            return self.bs(nums,pivot+1,n,target)
        else:
            return ret


arr=[1,2,5]
sol=Solution()

print sol.search(arr,3)
