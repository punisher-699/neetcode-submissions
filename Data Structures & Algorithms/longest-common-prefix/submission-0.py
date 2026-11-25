class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""
        mlen = len(min(strs))
        for i in range(mlen):
            cur = strs[0][i]
            for st in strs:
                if st[i] != cur:
                    return res
            res += cur
        
        return res

