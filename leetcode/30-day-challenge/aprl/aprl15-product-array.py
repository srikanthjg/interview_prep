class Solution(object):
    def productExceptSelf1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        op=[0]*len(nums)

        ####
        #product of all divided by itself
        ####
        for i in range(len(nums)):
            product=1
            for j in range(len(nums)):
                    if j == i:
                        continue
                    product = product*nums[j]

            op[i]=product
        return op
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L=[0]*len(nums)
        L[0]=1
        for i in range(1,len(nums)):
            L[i]=L[i-1]*nums[i-1]

        R=[0]*len(nums)
        R[-1]=1
        for i in range(len(nums)-2,-1,-1):
            R[i]=R[i+1]*nums[i+1]

        op=[0]*len(nums)
        for i in range(len(nums)):
            op[i]=L[i]*R[i]

        print L,R,op

        return op

nums=[1,2,3,4,5]
sol=Solution()
print sol.productExceptSelf(nums)
