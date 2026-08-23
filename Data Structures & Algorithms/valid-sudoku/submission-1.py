class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rht = defaultdict(set)
        cht = defaultdict(set)
        bht = defaultdict(set)

        for i in range(9):
            for j in range(9):

                if board[i][j] >= '1' and board[i][j] <= '9':
                    if (board[i][j] in rht[i] or board[i][j] in cht[j] or 
                        board[i][j] in bht[(i // 3, j // 3)]):
                        return False
                    rht[i].add(board[i][j])
                    cht[j].add(board[i][j])
                    bht[(i // 3, j // 3)].add(board[i][j])

        return True

                