#https://leetcode.com/problems/trapping-rain-water/
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<=2:
            return 0

        lmax=[0 for i in range(len(height))]
        rmax=[0 for i in range(len(height))]

        #container
        lm=height[0]
        lmax[0]=lm
        for i in range(0,len(height)-1,1):
            lm=max(height[i],lm)
            lmax[i]=lm
        #print lmax

        rm=height[len(height)-1]
        rmax[len(height)-1]=rm
        for i in range(len(height)-2,-1,-1):
            rm=max(rm,height[i])
            rmax[i]=rm
        #print rmax

        ans=0
        #count=0
        for i in range(len(height)):
            if lmax[i]>height[i] and rmax[i]>height[i]:
                #count+=1
                tmp=min(lmax[i],rmax[i])-height[i]
                ans+=tmp
                #print "i=%r,tmp=%d,lmax=%r,rmax=%r,height=%r"%(i,tmp,lmax[i],rmax[i],height[i])
        #print ans
        return ans
