direc=[(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
board=[[0 for i in range(3)]for j in range(3)]
print board

r,c=0,0
d=[1,1]
#for d in direc:
#

newr,newc=r+d[0],c+d[1]
while  newr<len(board) and newr>=0  and \
    newc<len(board) and newc>=0:

    board[newr][newc]+=1
    newr,newc=newr+d[0],newc+d[1]

print board
