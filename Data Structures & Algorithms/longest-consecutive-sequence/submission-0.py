class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numbers = set(nums)
        res = 0

        for num in numbers:
            if num-1 not in numbers:
                currl = 1
                while currl + num in numbers:
                    currl += 1
                res = max( res, currl)
        return res
            