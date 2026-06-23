class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        res = {}

        for s in strs:
            ht = [0] * 26
            for ch in s:
                ht[ord(ch) - ord('a')] += 1
            res[tuple(ht)] = res.get(tuple(ht) , []) + [s]
        return list(res.values())