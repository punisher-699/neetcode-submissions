class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        
        temp = prices[:]
        stack = []

        for i, p in enumerate(prices):
            while stack and prices[stack[-1]] >= p:
                temp[stack.pop()] -= p
            stack.append(i)
        return temp
