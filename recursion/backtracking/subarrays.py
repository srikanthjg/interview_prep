

def subarray_rec(A,out):
    print out
    if len(A)==0:
        return

    for i in range(len(A)):

        a=list(A)
        subarray_rec(A[1:],out+A[i])




##Do with backtracking

def subarray(A):
        output = ""
        subarray_rec(A,output)
        return output

A = "123"
out = subarray(A)
#print out
