#https://leetcode.com/problems/prison-cells-after-n-days/solution/
class Solution(object):
    def nxtDay(self,cells):
        cells_copy=cells[:]
        cells_copy[0]=0
        cells_copy[len(cells)-1]=0
        for i in range(1,7,1):
            if cells[i-1]==cells[i+1]:
                cells_copy[i]=1
            else:
                cells_copy[i]=0
        cells=cells_copy
        return cells

    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """

        day=0
        n=len(cells)
        seen=set()
        cycle=False
        while day<N:
            next=self.nxtDay(cells)
            tup=tuple(next)
            if tup in seen:
                cycle=True
                break
            seen.add(tup)
            cells=next
            day+=1

        #print day
        if cycle:
            N=N%(day)
            for i in range(N):
                cells=self.nxtDay(cells)
        return cells

sol=Solution()
cells=[1,0,0,1,0,0,1,0]
N=1000000000
print sol.prisonAfterNDays(cells, N)
