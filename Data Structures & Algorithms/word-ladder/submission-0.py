from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0

        nbs = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                nbs[pattern].append(word)
        

        visited = set([beginWord])
        q = deque([beginWord])
        
        res = 1
        
        while q:
            for i in range(len(q)):
                curword = q.popleft()
                
                if curword == endWord:
                    return res
                
                for j in range(len(curword)):
                    pat = curword[: j] + "*" + curword[j + 1: ]
                    for nb in nbs[pat]:
                        if nb not in visited:
                            visited.add(nb)
                            q.append(nb)
            res += 1
        return 0
