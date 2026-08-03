class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for ch in strs:
            ht = [0] * 26
            for c in ch:
                ht[ord(c) - ord('a')] += 1
            res[tuple(ht)] = res.get(tuple(ht), []) + [ch]
        return list(res.values())
            
            