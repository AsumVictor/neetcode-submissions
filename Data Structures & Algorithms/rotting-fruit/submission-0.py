class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        rotten = []
        fresh_fruits = 0

        # collect all the sources of the rotten fruits
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i, j))

                if grid[i][j] == 1:
                    fresh_fruits += 1

        # track, time
        time = 0
        queue = deque(rotten)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue and fresh_fruits > 0:

            # collect all items in the queue
            length = len(queue)
            time += 1
            for _ in range(length):

                # pop and infect
                i, j = queue.popleft()

                for r, c in directions:
                    nr, nc = r + i, j + c

                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue
                    
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh_fruits -= 1
        
        return -1 if fresh_fruits > 0 else time

                    








        