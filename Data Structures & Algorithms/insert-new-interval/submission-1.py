class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        a, b = newInterval[0], newInterval[1]
        for i, (st, end) in enumerate(intervals):
            if st > b:
                res.append(newInterval)
                return res + intervals[i : ]
            elif st < a:
                res.append(intervals[i])
            else:
                ni = [min(a, st), max(b, end)]
        res.append(ni)
        return res

