class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ht = []
        for i in nums:
            if i in ht:
                return True
            ht.append(i)
        return False
        