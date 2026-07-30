class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        def explore_land(i, j):

            # bounfries
            if i < 0 or j < 0 or i >= n or j >= m:
                return 0


            # check for 0 return 0 area
            if grid[i][j] == 0:
                return 0

            # visit the currne place
            # mark as water
            grid[i][j] = 0


            # explore all direction
            # get totoal szie
            size = 1
            for rw, rc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                size += explore_land(i + rw, j + rc)

            
            return size

        max_land = 0
        for i in range(n):
            for j in range(m):

                if grid[i][j] == 1:
                    max_land = max(max_land, explore_land(i, j))
        
        return max_land
                    



            # return size from childern



        