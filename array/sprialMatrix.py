
def spiralMatrix(input):
	arr=[[0]*input]*input
	dir = [(0,1),(1,0),(0,-1),(-1,0)]
	row=0
	col=0
	count=1
	direction=0
	row_start=0
	row_end=
	for i in range(input*input):

			print "row=%d,col=%d,count=%d,dir=%d"%(row,col,count,direction)
			arr[row][col] = count
			row = row+dir[direction][0]
			col = col+dir[direction][1]
			count=count+1

			if(count%(input)==0):
				direction=(direction+1)%4

	return arr


print spiralMatrix(4)
