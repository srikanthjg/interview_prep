class Solution(object):
    def getMsb(self,num):
        return int(str(num)[0])

    def sortByMSB(self,arr):
        msb_arr=[]
        max=-1
        for num in arr:
            msb = self.getMsb(num)
            if msb >max:
                max=msb


    def makeLargestNumber(self,arr):
        msb_arr = sortByMSB(arr)
        return msb_arr
