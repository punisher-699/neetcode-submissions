class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dr = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        q = deque()

        fresh = time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        
        while fresh > 0 and q:

            length = len(q)
            for i in range(length):

                row, col = q.popleft()
                for dx, dy in dr:
                    x = dx + row
                    y = dy + col

                    if (x in range(rows) and y in range(cols) and grid[x][y] == 1):
                        grid[x][y] = 2
                        q.append([x, y])
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1



        

            

                
            