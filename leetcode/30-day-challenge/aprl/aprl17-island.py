class Solution(object):

    def getUnvisitedLands(self, grid):

        unvisitedLands = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    unvisitedLands[(i,j)] = True

        return unvisitedLands

    def traverseLand(self, land_i, \
        land_j, max_i, max_j, grid, unvisitedLandsDict):

        directions = [[-1,0], [0,1], [1,0],[0,-1]]

        #mark this as visited

        if grid[land_i][land_j] == '0':
                      return

        if (land_i, land_j) not in unvisitedLandsDict:
                      return

        #if (land_i,land_j) in unvisitedLands:
        popped = unvisitedLandsDict.pop((land_i, land_j))

        print "popped (%d, %d) %r"%(land_i, land_j, popped)

        for direc in directions:
            new_x = land_i + direc[0]
            new_y = land_j + direc[1]

            if new_x < max_i and new_x >= 0 and new_y < max_j and new_y >= 0:
                self.traverseLand(new_x, new_y, max_i, max_j, grid, unvisitedLandsDict)



    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0

        unvisitedLandsDict = self.getUnvisitedLands(grid)

        if len(grid) == 0:
            return 0

        max_i = len(grid)
        max_j = len(grid[0])

        print "Unvisited lands %r, max_i %d max_j %d unvisitedLandsDict"%(
                unvisitedLandsDict, max_i, max_j)

        while True:
            if len(unvisitedLandsDict) == 0:
                      break

            next_land = unvisitedLandsDict.keys()[0]
            land_x, land_y = next_land

            self.traverseLand(land_x, land_y, max_i, max_j, grid, unvisitedLandsDict)
            islands += 1


        return islands
