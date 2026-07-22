class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        # ans = nums + nums
        # return ans
        n = len(nums)
        for i in range(2 * n):
            ans.append(nums[i % n])
        return ans