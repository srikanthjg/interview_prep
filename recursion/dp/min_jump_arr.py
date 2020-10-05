
def min_jump(A):
    minjump=99999
    target = len(A)-1

    num_jumps=0
    for i in range(len(A)):
        cur=i
        for j in range(i,len(A)):
            if(j+A[j]==target):
                


A = [2,3,1,1,4]
print min_jump(A)
