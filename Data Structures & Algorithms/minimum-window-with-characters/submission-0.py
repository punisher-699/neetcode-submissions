class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        #tt = set(t)

        #freq count mf

        freq = {}
        for ch in t:
            freq[ch] = 1 + freq.get(ch , 0)
        #This will contain all the chars from first occurence of any char from t

        res = []
        for ch in s:
            if ch in t:
                res.append(ch)
            else:
                if res:
                    res.append(ch)

        #This is going to remove all the non t chars from the end

        for i in range(len(res) - 1 , -1 , -1):
            if res[i] not in t:
                del res[i]
            else: break
            
        #now to be sure that every char of t has appeared in s we iterate over the
        #updated res and return the str if yes or ""

        for ch in t:
            if ch not in res:
                return ""
        n = len(res)
        for i,ch in enumerate(res):
            countc = 1
            if i + 1 < n:
                
                for j in range(i+1 , n):
                    if res[j] == ch:
                        countc += 1
            if countc > freq[ch]:
                del res[i]
        return ''.join(res)