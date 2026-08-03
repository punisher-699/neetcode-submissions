class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s or not t:
            return True
        if len(t) < len(s):
            return False
        
        sindex = 0
        temp = ""
        for ch in t:
            if ch in s[sindex]:
                sindex += 1
                temp += ch
        
        return temp == s