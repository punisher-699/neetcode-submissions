class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if not s:
            return True
        
        sindex = 0

        for ch in t:
            if ch == s[sindex]:
                sindex += 1
                if sindex == len(s):
                    return True
        return False