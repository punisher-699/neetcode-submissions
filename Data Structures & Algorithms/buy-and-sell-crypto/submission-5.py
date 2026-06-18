class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxp = 0
        bp = 0 
        
        for sp in range(1, len(prices)):
            if prices[sp]  < prices[bp]:
                bp = sp
            else:
                maxp = max(maxp , prices[sp] - prices[bp])
            
        return maxp