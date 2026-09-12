class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        dr = ((-1, 0), (0, 1), (1, 0), (0, -1))
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prevH):
            if ((r, c) in visited or r < 0 or c < 0 or r >= rows or c >= cols or prevH > heights[r][c]):
                return
            visited.add((r, c))
            for x, y in dr:
                dfs(x + r, y + c, visited, heights[r][c])
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
                

