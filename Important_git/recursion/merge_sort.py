def merge(A,l,r,mid):

    len_l = mid-l+1
    len_r = r-mid
    i=j=k=0
    L=[-1]*len_l
    R=[-1]*len_r
    #print "l=%d,r=%d,mid=%d,len_l=%d,lenr=%d"%(l,r,mid,len_l,len_r)
    for i in range(len_l):
        L[i] = A[l+i]

    for j in range(len_r):
        R[j] = A[mid+1+j]

    i=j=0
    k=l
    while(i<len_l and j<len_r):
        if L[i]<=R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1
        k+=1

    while(i<len_l):
        A[k] = L[i]
        i+=1
        k+=1

    while(j<len_r):
        A[k] = R[j]
        j+=1
        k+=1
    #print A,L,R
    #print "l=%d,mid=%d,r=%d,i=%d,j=%d,k=%d"%(l,mid,r,i,j,k)
    return



def merge_sort(A,l,r):
    if l>=r:
        return
    mid = (l+r)//2
    merge_sort(A,l,mid)
    merge_sort(A,mid+1,r)
    merge(A,l,r,mid)
    return

A = [4,1,5,3,7,4]
merge_sort(A,0,len(A)-1)
print A
