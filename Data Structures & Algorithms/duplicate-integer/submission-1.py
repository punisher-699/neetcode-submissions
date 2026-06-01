class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ht = set()

        for i in nums:
            if i in ht:
                return True
            ht.add(i)
        return False