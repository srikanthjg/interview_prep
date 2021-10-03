import itertools

st = "ABC"
per = itertools.permutations(st,2)
com=itertools.combinations(st,2)
#print list(per)
#print list(com)

def ch(arr,r,chosen,out):
    if len(chosen)==r:
        out.append(chosen[:])
        return

    for i in range(len(arr)):
        chosen.append(arr[i])
        ch(arr[i+1:],r,chosen,out)
        chosen.pop()

def combinations(arr,r):
    out=[]
    ch(arr,r,[],out)
    return out

def ph(arr,r,chosen,out):
    if len(chosen)==r:
        out.append(chosen[:])
        return

    for i in range(len(arr)):
        tmp=arr.pop(i)
        chosen.append(tmp)
        ph(arr,r,chosen,out)
        chosen.pop()
        arr.insert(i,tmp)

def permutations(arr,r):
    out=[]
    ph(arr,r,[],out)
    return out


arr=[1,2,3,4]
#print permutations(arr,2)
print combinations(arr,2)
