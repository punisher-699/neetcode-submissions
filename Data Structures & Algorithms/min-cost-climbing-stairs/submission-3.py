class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost_len = len(cost)

        two = cost[cost_len - 1]
        one = cost[cost_len - 2]

        for i in range(cost_len - 3, -1, -1):
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])
        
        return min(cost[0], cost[1])

