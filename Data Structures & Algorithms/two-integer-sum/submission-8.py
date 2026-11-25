class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap = {}
        hset = set()
        for i in range(len(nums)):
            if (target - nums[i]) in hset:
                return [hmap[target - nums[i]], i]
                
            hset.add(nums[i])
            hmap[nums[i]] = i

        return []
