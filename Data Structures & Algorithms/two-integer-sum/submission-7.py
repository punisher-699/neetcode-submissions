class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap = {}
        hset = set()
        for i in range(len(nums)):
            if (target - nums[i]) in hset:
                res = [hmap[target - nums[i]], i]
                return res
            hset.add(nums[i])
            hmap[nums[i]] = i

        return []
