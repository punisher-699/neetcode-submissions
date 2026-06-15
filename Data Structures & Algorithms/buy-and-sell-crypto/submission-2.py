class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxp = 0
        bp , sp = 0 , 1
        while bp <= len(prices) - 1 and sp <= len(prices) - 1:
            cost =  prices[sp] - prices[bp]
            if cost > maxp:
                maxp = cost
                sp += 1
            else :
                if prices[sp] > prices[bp]:
                    sp += 1
                else :
                    sp += 1
                    bp += 1

            
        return maxp