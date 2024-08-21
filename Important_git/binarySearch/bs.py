class BinarySearch():
    def bs(self,arr,val,l,r):
        if l>r:
            return -1
        mid=(l+r)//2
        if val==arr[mid]:
            return mid
        if val<arr[mid]:
            return self.bs(arr, val, l, mid-1)
        return self.bs(arr,val,mid+1,r)

    def findPeak(self,arr):



sol=BinarySearch()
arr=[1,2,4,5,8]
print sol.bs(arr,4,0,len(arr)-1)
