class Solution:
    def rob(self, nums: List[int]) -> int:

        one = nums[0]
        two = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            cur = max(nums[i] + one, two)
            one = two
            two = cur
        return two
        
    
            
