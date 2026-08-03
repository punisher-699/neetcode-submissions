class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        pref = [0] * (len(words) + 1)
        vset = set("aeiou")

        prev = 0
        for i, word in enumerate(words):
            if word[0] in vset and word[-1] in vset:
                prev += 1
            pref[i + 1] = prev
        

        res = []
        for st, end in queries:
            
            res.append(pref[end + 1] - pref[st])
        
        return res
