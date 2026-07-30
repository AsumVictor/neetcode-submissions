class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # collect all the sources
        INF = 2147483647
        sources = []
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    sources.append((i, j, 0))
        

        # start a queue at the sources
        queue = deque(sources)
        directions = [(1, 0),(-1, 0), (0, 1), (0, -1)]

        while queue:
            i,j,dist = queue.popleft()

            for r, c in directions:
                nr, nc = i + r, j + c

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                
                if grid[nr][nc] == INF:
                    # replace with distace
                    grid[nr][nc] = dist + 1
                    queue.append((nr, nc, dist + 1))


        

