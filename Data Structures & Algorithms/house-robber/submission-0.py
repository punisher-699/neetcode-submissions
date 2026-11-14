class Solution:
    def rob(self, nums: List[int]) -> int:
        
        odd, even = 0, 0
        n = len(nums)
        for i in range(n):
            if i % 2 == 0:
                even += nums[i]
            else:
                odd += nums[i]
        return max(odd, even)