class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        arr = []
        laste = intervals[0]
        for i, (st, end) in enumerate(intervals):
            if st <= laste[1]:
                laste[1] = max(laste[1], end)
            else:
                arr.append(laste)
                laste = [st, end]
        arr.append(laste)
        return arr