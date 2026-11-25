class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        li = len(nums) - 1
        n = len(nums)
        k = 0
        i = 0
        while i < (n - k):
            if nums[i] == val:
                nums[i], nums[li] = nums[li], nums[i]
                li -= 1
                k += 1
            else:
                i += 1
        
        return n - k