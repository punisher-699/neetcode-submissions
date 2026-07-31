class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 1:
            return 0
        count = 0
        j = len(nums) - 1
        i = 0
        while i <= j:
            if nums[i] == val:
                while j >= i and nums[j] == val:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                count += 1
                j -= 1
            i += 1
        return i