class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n = len(grid)
        m = len(grid[0])


        # explore the lan
        def explore_land(i, j):
            # check boundries
            if i < 0 or j < 0 or i >= n or j >= m:
                return
            
            # check water
            if grid[i][j] == "0":
                return
            
            # explore the land
            grid[i][j] = "0"

            # explore the neibhors
            # top
            explore_land(i - 1, j)

            # buttom
            explore_land(i + 1, j)

            # left
            explore_land(i, j - 1)

            # right
            explore_land(i, j + 1)

            return

        total = 0
        for i in range(n):
            for j in range(m):

                if grid[i][j] == "1":
                    total += 1
                    explore_land(i, j)

        return total
        