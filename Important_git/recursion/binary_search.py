def binary_search(A,l,r,target):
    if l>r:
        return -1

    mid = (l+r)//2
    if(A[mid] == target):
        return mid
    elif target<A[mid]:
         return binary_search(A,l,mid-1,target)
    else:
        return binary_search(A,mid+1,r,target)
    return

A = [1,4,5,7,8,9]
print binary_search(A,0,len(A)-1,4)
