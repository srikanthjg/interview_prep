def partition(A,l,r):
    pivot = r

    i=l-1

    #till last -1
    for j in range(l,r):
        if A[j] < A[pivot]:
            i+=1
            A[i],A[j] = A[j],A[i]


    A[i+1],A[pivot] = A[pivot],A[i+1]
    pivot = i+1
    print "A=%r,l=%d,r=%d,A[%d]=%d"%(A,l,r,A[pivot],pivot)
    return pivot

def quick_sort(A,l,r):
    if l>=r:
        return
    pivot = partition(A,l,r)
    quick_sort(A,l,pivot-1)
    quick_sort(A,pivot+1,r)

A = [3,2,1,4,8,5]

quick_sort(A,0,len(A)-1)
print A
