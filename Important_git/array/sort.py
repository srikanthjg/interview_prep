

def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A)-i):
            if(A[j]>A[i]):
                A[i],A[j] = A[j],A[i]

    return A

def insertion_sort(A):
    pass

def count_sort(A):
    arr = [0]*100
    output = []
    for i in range(len(A)):
        arr[A[i]]+=1
    #print arr
    for i in range(len(arr)):
        if(arr[i]!=0):
            while arr[i]!=0:
                output.append(i)
                arr[i]-=1

    print output


def count_sort_radix(A,exp,max):
    pass

def radix_sort(A):
    return A


def partition(A,l,r):
    #assume pivot is the leftmost
    pivot = A[r]
    #i will be left of pivot
    #j will be right of pivot
    i=l-1
    #print "in partition"
    #print A
    for j in range(l,r):
        if(A[j]<pivot):
            i+=1
            A[j],A[i] = A[i],A[j]
            #print A
    #swap i with pivot to get to the final position of pivot --> all i < pivot < j
    i+=1
    A[i],A[r] = A[r],A[i]
    return i

def quick_sort(A,l,r):
    if(l>=r):
        return

    pivot = partition(A,l,r)
    quick_sort(A,l,pivot-1)
    quick_sort(A,pivot+1,r)
    return A

def merge_sort(A,l,r):
    if(l<r):
        output = []
        mid = (l+r)//2
        L = A[:mid] #exclude mid
        R = A[mid:] #include mid

        merge_sort(L,l,mid)
        merge_sort(R,mid+1,r)

        #merge logic
        j=0 #L
        k=0 #R

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i+=1
            else:
                A[k] = R[j]
                j+=1
            k+=1

        # Checking if any element was left
        while i < len(L):
            A[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            A[k] = R[j]
            j+=1
            k+=1

        return A


A = [15,4,27,1,48]

#print  quick_sort(A,0,len(A)-1)
print merge_sort(A,0,len(A)-1)
