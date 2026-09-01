class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}

        for word in strs:
            ht = [0] * 26
            for ch in word:
                #ht[ch] = ht.get(ch, 0) + 1
                ht[ord(ch) - ord('a')] += 1
            res[tuple(ht)] = res.get(tuple(ht), []) + [word]
        return list(res.values())
            