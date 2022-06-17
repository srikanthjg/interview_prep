a=[1,2,2,2,2,3]
l=0
r=1

def findlr(nums,mid):
    l=mid
    r=mid

    #go right
    while r<=len(nums) and nums[l] == nums[r]:
        r+=1
    r-=1

    #go left
    while l>=-1 and nums[l] == nums[r]:
        l-=1
    l+=1
    return [l,r]

print(findlr(a,4))
"""
for i in range(len(a)):
    if r==len(a):
        print (l,r-1,i)
        break
    if a[l]!=a[r]:
        print(l,r-1,i)
        l=r
        r+=1
    else:
        r+=1
    i+=1
"""
