class Solution:
    
    def characterReplacement(self, s: str, k: int) -> int:
        
        freqt = {}
        left = 0
        res = 0
        for right in range(len(s)):
            freqt[s[right]] = 1 + freqt.get(s[right],0)
            

            while (right - left + 1) - max(freqt.values()) > k:
                freqt[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        return res
            
            

           

