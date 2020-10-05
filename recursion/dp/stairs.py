out=[]

def stairs_helper(n,sum,output):
    if sum==n:
        print output
        return
    if sum >n:
        return

    #print sum,output
    stairs_helper(n,sum+1,output+'1')
    stairs_helper(n,sum+2,output+'2')


def stairs(n):
    stairs_helper(n,0,"");
    return

print stairs(4)
