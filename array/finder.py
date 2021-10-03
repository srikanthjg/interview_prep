def finder(a,b):
    b = sorted(b)
    print b
    for i in range(len(b)):
        if a[i] != b[i]:
            return a[i]


print finder([1,2,3,4],[4,1,3])
