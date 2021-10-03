

def bubble_sort(A):
    for i in range(0,len(A)):
        for j in range(0,len(A)-1-i):
            if(A[j]>A[j+1]):
                A[j+1],A[j] = A[j],A[j+1]

    return A

def insertion_sort(A):
    pass

def count_sort(A,k):
    count = [0 for i in range(k)]
    output = [0 for i in range(len(A)+1)]
    for i in range(len(A)):
        count[A[i]]+=1
    #print arr

    """
    for i in range(len(arr)):
        if(arr[i]!=0):
            while arr[i]!=0:
                output.append(i)
                arr[i]-=1
    """

    for i in range(1,len(count)):
        count[i]+=count[i-1]

    print output,count
    for i in range(len(A)-1,-1,-1):
        output[count[A[i]]]=A[i]
        count[A[i]]-=1

    print output[1:]


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

def merge_sort(A):
    if(len(A)>1):
        mid = (len(A))//2
        L = A[:mid] #exclude mid
        R = A[mid:] #include mid

        merge_sort(L)
        merge_sort(R)

        #merge logic
        i=0 #L
        j=0 #R
        k=0 #A

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


A = [8,5,3,2,8]

#print  quick_sort(A,0,len(A)-1)
print merge_sort(A)
#print count_sort(A,10)
