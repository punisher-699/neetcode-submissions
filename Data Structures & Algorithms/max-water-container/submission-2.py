class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        i = 0 ; j = len(heights) - 1
        max = 0
        while i < j:
            vol = min(heights[i] , heights[j]) * abs(i - j)

            if vol > max : max = vol
            if heights[i] < heights[j] :
                i += 1
            else: j -= 1
        return max
