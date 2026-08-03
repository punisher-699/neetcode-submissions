class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s:
            return True
        if not t:
            return False
        if len(t) < len(s):
            return False
        slen = len(s)
        sindex = 0
        temp = ""
        for ch in t:
            if sindex < slen and ch == s[sindex]:
                sindex += 1
                temp += ch
        
        return temp == s