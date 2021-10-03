#https://www.youtube.com/watch?v=bqN9yB0vF08

class Solution(object):
    """
    def sum1(self,i,j,cum_sum):
        if i==0:
            return cum_sum[j]
        return cum_sum[j]-cum_sum[i-1]
    """
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        #O(N^2)
        cum_sum=[0 for i in range(len(nums))]
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            cum_sum[i]=s
        #print cum_sum
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                n=self.sum1(i,j,cum_sum)
                #print n,i,j
                if n==k:
                    count+=1
        return count
        """

        #O(N)
        prefix_map={0:1} # this is for one element with cur_sum==k
        cur_sum=0
        count=0

        for n in (nums):
            cur_sum+=n

            if cur_sum-k in prefix_map:
                count+=prefix_map[cur_sum-k]

            if cur_sum not in prefix_map:
                prefix_map[cur_sum]=1
            else:
                prefix_map[cur_sum]+=1


        return count
