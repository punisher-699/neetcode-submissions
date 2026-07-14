class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        dr = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == "0"):
                return
            grid[r][c] = "0"
            for dx, dy in dr:
                nr = r + dx
                nc = c + dy

                #if 0 <= nr < m and 0 <= nc < n:
                dfs(nr, nc)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        return res


