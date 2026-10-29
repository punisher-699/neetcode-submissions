class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        hset = set()
        for i in range(len(nums)):
            if target - nums[i] in hset:
                return [dic[target - nums[i]], i]
            hset.add(nums[i])
            dic[nums[i]] = i
        return []