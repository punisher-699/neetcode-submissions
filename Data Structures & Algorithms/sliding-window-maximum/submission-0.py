class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        maxval = float('-inf')
        res = []
        l = 0
        length = 0
        for r, num in enumerate(nums):
            length = r - l + 1
            maxval = max(maxval, num)
            if length < k:
                continue
            if length == k:
                res.append(maxval)
                maxval = max(nums[l + 1: r + 1])
                l += 1
        return res
            
            