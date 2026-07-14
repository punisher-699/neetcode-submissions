class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        mylist = intervals[:]
        mylist.append(newInterval)
        mylist.sort()
        res = []
        prev = mylist[0]

        for st, end in mylist[1:]:

            if st <= prev[1]:
                prev[1] = max(prev[1], end)
            else:
                res.append(prev)
                prev = [st, end]
        res.append(prev)
        return res

