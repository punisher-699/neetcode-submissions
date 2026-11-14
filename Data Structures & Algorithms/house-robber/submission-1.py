class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        def f(i):
            if i >= n:
                return 0
            return max(f(i + 1), nums[i] + f(i + 2))
        return f(0)
