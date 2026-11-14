class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        n = len(nums) 
        #nums[0] = max(nums[0], nums[-1])
        #n = n - 1

        dp = [0] * (n - 1)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n - 1):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        ans = dp[-1]

        dp = [0] * (n - 1)
        dp[0] = nums[1]
        dp[1] = max(nums[1], nums[2])
        for i in range(3, n):
            dp[i - 1] = max(nums[i] + dp[i - 3], dp[i - 2])

        return max(dp[-1], ans)