##ITERATIVE SEGMENT TREE

"""
Time Complexity:
Tree Building: O(N)
Update and Search: O(LogN)
"""

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.tree=[0 for i in range( 2*len(nums))]
        self.size=len(nums)

        #build tree
        for i in range(len(nums)):
            self.tree[i+self.size]=nums[i]

        #reverse because we have to build the tree ground up
        ###NOTE it is till 0 not -1
        for i in range(len(nums)-1,0,-1):
            self.tree[i]=self.tree[2*i]+self.tree[(2*i) +1]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        pos=i+self.size
        self.tree[pos]=val
        while pos>0:
            if pos%2==0:
                left=pos
                right=pos+1
            else:
                left=pos-1
                right=pos
            pos/=2
            self.tree[pos]=self.tree[left]+self.tree[right]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        l=i+self.size
        r=j+self.size
        sum=0
        while l<=r:
            if l%2!=0:
                sum+=self.tree[l]
                l+=1 #we dont want to include the l of the previous node; 1,2,3: if 2 is left node,
                     #we dont want to include 1 in the sum range
            if r%2==0:
                sum+=self.tree[r]
                r-=1
            l/=2
            r/=2
        return sum


############## 2D MATRIX ##########
class SegmentTree2D():
    def __init__(self, matrix):
        self.R, self.C = len(matrix), len(matrix[0])
        self.tree = [[0] * (2*self.C) for _ in range(self.R)]

        # copy leaf nodes
        for r in range(self.R):
            for i in range(self.C):
                self.tree[r][self.C+i] = matrix[r][i]

        # create child nodes
        for r in range(self.R):
            for i in reversed(range(1, self.C)):    # i have kids 2i+1, 2i+2, same as in case of heap
                self.tree[r][i] = self.tree[r][i<<1] + self.tree[r][i<<1 | 1]

    # update value
    def update(self, row, col, val):
        i = self.C + col
        self.tree[row][i] = val
        i = i >> 1
        while i:
            self.tree[row][i] = self.tree[row][i<<1] + self.tree[row][i<<1 | 1]
            i = i>>1

    # get value
    def get(self, r1, c1, r2, c2):
        ans = 0
        for row in range(r1, r2+1):  #===>  only thing extra
            l = self.C+c1
            r = self.C+c2+1 # r not inclusive

            while l<r:
                if l & 1:
                    ans += self.tree[row][l]
                    l += 1
                if r & 1:
                    r -= 1
                    ans += self.tree[row][r]

                l = l>>1
                r = r>>1
        return ans

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return

        self.segment = SegmentTree2D(matrix)
        self.matrix = matrix

    def update(self, row: int, col: int, val: int) -> None:
        self.segment.update(row, col, val)
        self.matrix[row][col] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # D - C - B + A
        return self.segment.get(row1, col1, row2, col2)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
