class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vlist = [0] * len(words)

        for i, word in enumerate(words):
            if word[0] in "aeiou" and word[-1] in "aeiou":
                vlist[i] = 1
        
        res = []
        for st, end in queries:
            count = 0
            for i in range(st, end + 1):
                if vlist[i]:
                    count += 1
            res.append(count)
        
        return res
