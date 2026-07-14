class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return[nums[i], nums[i] + 1]
                