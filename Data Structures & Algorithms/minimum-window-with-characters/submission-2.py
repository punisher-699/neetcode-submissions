class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "": return ""

        #freq
        freq = {} 
        for ch in t:
            freq[ch] = 1 + freq.get(ch, 0)
        have , need = 0 , len(freq)
        res , resl = [-1 , -1] , 1001
        left = 0
        window = {}
        for right in range(len(s)):

            window[s[right]] = 1 + window.get(s[right], 0)

            if s[right] in t and window[s[right]] == freq[s[right]]:
                have += 1
            
            while have == need:
                if right - left + 1 < resl:
                    res = [left , right]
                    resl = right - left + 1
                
                window[s[left]] -= 1
                if s[left] in freq and window[s[left]] < freq[s[left]]:
                    have -= 1
                left += 1

        left , right = res
        return s[left : right + 1] if resl != -1 else ""