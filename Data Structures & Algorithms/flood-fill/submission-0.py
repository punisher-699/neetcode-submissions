class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        dr = ((0, 1), (1, 0), (-1, 0), (0, -1))

        rows, cols = len(image), len(image[0])
        cur_color = image[sr][sc]

        if cur_color == color:
            return image
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != cur_color:
                return
            
            image[r][c] = color
            for x, y in dr:
                dfs(x + r, y + c)
            
        dfs(sr, sc)
        return image