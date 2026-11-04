class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        dr = (
             (1, 0), 
             (-1, 0),
             (0, -1), 
             (0, 1)
        )
        def dfs(i, j, cword):
            if i not in range(rows) or j not in range(cols):
                return False
            if board[i][j] != cword[0]:
                return False
            if len(cword) == 1:
                return True
                
            
            og = board[i][j]
            board[i][j] = "#"
            for x, y in dr:
                if dfs(i + x, j + y, cword[1:]):
                    board[i][j] = og
                    return True
            board[i][j] = og
            return False

            
        tword = word[:]
        for i in range(rows):
            for j in range(cols):

                if dfs(i, j, word):
                    return True
        return False
