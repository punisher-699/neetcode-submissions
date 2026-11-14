class Solution:
    def climbStairs(self, n: int) -> int:
        
        ostep = tstep = 1

        cur = 0
        for i in range(n - 1):
            cur = ostep + tstep
            tstep = ostep
            ostep = cur
        
        return ostep