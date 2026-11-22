class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        a, b = newInterval[0], newInterval[1]
        for i, (st, end) in enumerate(intervals):
            if st > b:
                res.append([a, b])
                return res + intervals[i : ]
            elif end < a:
                res.append(intervals[i])
            else:
                a = min(a, st)
                b = max(b, end)
        res.append([a, b])
        return res

