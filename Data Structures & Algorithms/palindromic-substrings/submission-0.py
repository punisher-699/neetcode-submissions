class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        slen = len(s)
        for i in range(slen):
            l, r = i, i
            while l >= 0 and r < slen and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
            
            l, r = i, i + 1
            while l >= 0 and r < slen and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
        return res
