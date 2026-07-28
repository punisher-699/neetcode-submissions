class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = res = -1001
        for num in nums:
            summ = max(num, summ + num)
            res = max(res, summ)
        
        return res