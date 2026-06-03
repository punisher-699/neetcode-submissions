class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}

        for i in range(len(nums)):
            com = target - nums[i]
            if com in ht:
                return [ht[com],i]
            ht[nums[i]] = i
            