
def spiralMatrix(input):
	arr=[[-1 for i in range(input)] for j in range(input)]
	dir = [(0,1),(1,0),(0,-1),(-1,0)]
	row=0
	col=0
	count=1
	direction=0
	for i in range(input*input):

			#print "row=%d,col=%d,count=%d,dir=%d"%(row,col,count,direction)
			arr[row][col] = count
			count=count+1
			r = (row+dir[direction][0])%input
			c = (col+dir[direction][1])%input

			if(arr[r][c]!=-1):
				direction=(direction+1)%4
				
			row=(row+dir[direction][0])%input
			col=(col+dir[direction][1])%input

	return arr

##ACCEPTED
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        #fill=range(1,n*n+1)
        matrix=[[float('inf') for i in range(n)] for j in range(n)]
        #print fill,matrix

        h=len(matrix)-1
        w=len(matrix)-1

        sr=0
        er=h
        sc=0
        ec=h
        dir=0
        val=1
        for _ in range(n*n):

            #right
            if dir==0:
                for i in range(sc,ec+1):
                    matrix[sr][i]=val
                    val+=1
                sr+=1

            #left
            elif dir==2:
                for i in range(ec,sc-1,-1):
                    matrix[er][i]=val
                    val+=1
                er-=1
            #row
            #down
            elif dir==1:
                for i in range(sr,er+1):
                    matrix[i][ec]=val
                    val+=1
                ec-=1
            #up
            elif dir==3:
                for i in range(er,sr-1,-1):
                    matrix[i][sc]=val
                    val+=1
                sc+=1
            #print matrix
            dir=(dir+1)%4

        return matrix
print spiralMatrix(4)
