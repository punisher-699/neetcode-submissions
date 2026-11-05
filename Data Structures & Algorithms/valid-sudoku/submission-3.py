class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        #Brute force , row by row and col by col then box by box
        r = [0] * 9
        c = [0] * 9
        b = [0] * 9
        for row in board:
            for i in row:
                if i != '.':
                    r[int(i) - 1] += 1
                    if r[int(i) - 1] > 1:
                        return False
            r = [0] * 9
        
        for i in range(0,9):
            for j in range(0,9):
                if board[j][i] != '.':
                    c[int(board[j][i]) - 1] += 1
                    if c[int(board[j][i]) - 1] > 1:
                        return False
            c = [0] * 9
        
        for s in range(9):
            b = [0] * 9
            for i in range(3):
                for j in range(3):
                    row = (s // 3) * 3 + i
                    col = (s % 3) * 3 + j
                    if board[row][col] != '.':
                        b[int(board[row][col]) - 1] += 1
                        if b[int(board[row][col]) - 1] > 1:
                            return False
        return True
