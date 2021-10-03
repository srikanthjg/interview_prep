import copy


## Use mirror logic
## append 0 to L1 and 1 to L2
def grey_code(n):
    L1=["0","1"]


    for i in range(1,n):
        L2 = L1[:]
        L2.reverse()

        #print "reversed L2: %r"%L2

        new_L1 = []
        for ele in range(len(L1)):
            new_L1.append("0"+L1[ele])

        for ele in range(len(L2)):
            new_L1.append("1"+L2[ele])

        L1 = new_L1

    return L1

print grey_code(3)
