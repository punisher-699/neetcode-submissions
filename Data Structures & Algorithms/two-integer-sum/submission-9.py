class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap = {}
        
        for i, num in enumerate(nums):
            temp = target - num
            if temp in hmap:
                return [hmap[temp], i]
            hmap[num] = i
        return []
