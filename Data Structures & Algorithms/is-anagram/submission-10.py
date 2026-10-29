class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ht = [0] * 26

        for chs, cht in zip(s, t):
            ht[ord(chs) - ord('a')] += 1
            ht[ord(cht) - ord('a')] -= 1
        
        for i in range(26):
            if ht[i] != 0:
                return False
        return True
        
