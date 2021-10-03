import copy

output=[]
mincost=9999
def rope(A1,A,cost):
    print A,cost,
    if len(A)==2:
        cost.append(A[0]+A[1])
        output.append(cost)
        #print cost
        #cost = []
        return

    for i in range(len(A)-2):
        #print A,cost
        a1=A[i]
        A.remove(A[i])
        for j in range(i,len(A)-1):
            #print i,j,A
            a2=A[j]
            A.remove(A[j])
            cost.append(a1+a2)
            A.insert(0,a1+a2)
            print a1,a2,i,j
            rope(A1,A,cost)
            #A.insert(i,a1)
            #A.insert(j,a2)
            cost=[]
            #A=copy.copy(A1)






A= [8,4,6,12]
A1=copy.copy(A)
rope(A1,A,[])
print output
