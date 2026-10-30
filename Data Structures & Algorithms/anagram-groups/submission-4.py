class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ht = {}
        for i in range(len(strs)):
            alp = [0] * 26
            for ch in strs[i]:
                alp[ord(ch) - ord('a')] += 1
            ht[tuple(alp)] = ht.get(tuple(alp), []) + [strs[i]]

        return list(ht.values())
            