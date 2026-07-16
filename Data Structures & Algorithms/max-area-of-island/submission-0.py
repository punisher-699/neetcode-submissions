class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = set()
        dr = (
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        )
        
        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))
            
        maxval = 0
        for i in range(row):
            for j in range(col):
                maxval = max(maxval, dfs(i, j))
        return maxval