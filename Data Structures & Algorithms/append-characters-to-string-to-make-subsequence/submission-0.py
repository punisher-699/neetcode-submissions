class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        i = 0
        for ch in s:
            if i < len(t) and t[i] == ch:
                i += 1
        
        return len(t) - i