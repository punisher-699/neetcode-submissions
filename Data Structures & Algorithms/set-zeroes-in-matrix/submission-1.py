class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])

        rows, cols = [False] * row, [False] * col
        
        for i in range(row):
            for j in range(col):

                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        for i in range(row):
            for j in range(col):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0

                    

        
        