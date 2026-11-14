class Solution:
    def rob(self, nums: list[int]) -> int:
        
        def helper(nums):
            if len(nums) == 1:
                return nums[0]

            n = len(nums)
            dp = [0] * n

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            
            return dp[-1]
        
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))