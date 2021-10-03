
hmap={}
def sum(a,b):

    if (a,b) in hmap:
        print "in"
        return hmap[(a,b)]
    print "out"
    c=a+b
    hmap[(a,b)]=c
    return c


c=sum(2,3)
c=sum(2,3)

res=[]
for i in range(4):
    arr=[]
    arr.append(i)
    res.append(arr)
print res

print "HI"
for i in range(0,9,3):
    for j in range(0,9,3):
        print i,j
