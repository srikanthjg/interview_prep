

## num_of_island is global because pass by reference of a varialbe doesnt work, we can use a list instead
num_of_island = 0
#check 4 sides
def checkNeighbour(A,i,j,groupnum):
    # 0<=i<=len(A[0])
    # 0<=j<=len(A)

    global num_of_island
    maxi = len(A)-1
    maxj = len(A[0])-1

    direction = [[-1,0],[1,0],[0,-1],[0,1]]
    #derive from older group_num
    for direc in direction:
        newi = i+direc[0]
        newj = j+direc[1]

        if newi>=0 and newi<=maxi and newj>=0 and newj <= maxj:
            if A[newi][newj] == '1' and groupnum[newi][newj]!=0:
                #print "i=%d,j=%d,newi=%d,newj=%d"%(i,j,newi,newj)
                groupnum[i][j] = groupnum[newi][newj]

    #new island
    if groupnum[i][j] == 0 and A[i][j]=='1':
        num_of_island += 1
        groupnum[i][j] = num_of_island
        return

    return

def island(A):
##groupnum=[[0]*len(A[0]]*range(len(A))
##`doesnt work as groupnum[0][0]=1 causes  [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]] `
        #groupnum=[[0]*len(A[0])]*len(A)
    groupnum = [ [0] * len(A[0]) for i in range(len(A)) ]
    #print groupnum[4][0]
    #print groupnum,len(A[0]),len(A)
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == '1':
                checkNeighbour(A,i,j,groupnum)

    return num_of_island

A = ['11010',
     '11010',
     '11000',
     '00000']
B=[ ["1","1","0","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]]

C= [["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]]
a=[["1","1","1"],["0","1","0"],["1","1","1"]]
print island(C)




"""
### Already part of an island    , get groupnum from neigh
#top    => i+!,j
#bottom => i-1,j
#left   => i,j-1
#right  => i,j+1
top    = (i-1)%len(A)
bottom = (i+1)%len(A)
left   = (j-1)%len(A[0])
right  = (j+1)%len(A[0])

#print "coordinate %d,%d"%(i,j)
#print "before groupnum %r"%(groupnum)
#print A[i][right],groupnum[i][right]
if (A[top][j]=='1' and groupnum[top][j]!=0):
    #print "top"
    #print " "
    groupnum[i][j] = groupnum[top][j]
    return
elif (A[bottom][j]=='1' and groupnum[bottom][j]!=0):
    #print "bottom"
    #print " "
    groupnum[i][j] = groupnum[bottom][j]
    return
elif (A[i][right]=='1' and groupnum[i][right]!=0):
    #print "right"
    #print " "
    groupnum[i][j] = groupnum[i][right]
    return
elif (A[i][left]=='1' and groupnum[i][left]!=0):
    #print "left"
    #print " "
    groupnum[i][j] = groupnum[i][left]
    return
"""
