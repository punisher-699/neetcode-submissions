class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        res = float('inf')
        nums.sort()
        l = 0
        for r in range(k - 1, len(nums)):

            diff = nums[r] - nums[l]
            res = min(res, diff)
            l += 1

        return res