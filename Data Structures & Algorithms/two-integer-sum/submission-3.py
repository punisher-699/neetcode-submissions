class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = defaultdict()
        hset = set()
        for i in range(len(nums)):
            if target - nums[i] in hset:
                return [dic[target - nums[i]], i]
            hset.add(nums[i])
            dic[nums[i]] = dic.get(nums[i], 0) 
        return []