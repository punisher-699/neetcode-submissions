class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        def costfun(i):
            if i >= n:
                return 0
            
            return cost[i] + min(costfun(i + 1), costfun(i + 2))
        
        return min(costfun(0), costfun(1))
