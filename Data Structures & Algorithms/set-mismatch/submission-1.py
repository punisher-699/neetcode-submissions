class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hset = set(nums)
        ht = set()
        res = [-1, -1]
        for i in range(1, len(nums) + 1):
            if i not in hset:
                res[1] = i
                break
        for num in nums:
            if num in hset:
                hset.remove(num)
            else:
                res[0] = num
                break
        return res