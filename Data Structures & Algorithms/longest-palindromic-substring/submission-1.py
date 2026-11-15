class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        slen = len(s)
        for i in range(slen):
            for j in range(i, slen):

                l, r = i, j
                flag = True
                while l < r:
                    if s[l] != s[r]:
                        flag = False
                        break
                    l += 1
                    r -= 1
                
                if flag and (j - i + 1) > len(res):
                    res = s[i : j + 1]
        return res