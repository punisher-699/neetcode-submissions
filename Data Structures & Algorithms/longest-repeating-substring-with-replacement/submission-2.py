class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        ft = {}
        l = 0
        res = 0
        for r in range(len(s)):
            ft[s[r]] = 1 + ft.get(s[r], 0)

            while (r - l + 1) - max(ft.values()) > k:
                ft[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res

            