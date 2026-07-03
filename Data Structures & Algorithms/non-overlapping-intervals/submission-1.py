class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        

        if not intervals or len(intervals) == 1:
            return 0
        
        intervals.sort()
        laste, count = intervals[0][1], 0

        for i, interval in enumerate(intervals):
            if i == 0:
                continue
            if interval[0] < laste:
                count += 1
                laste = min(laste, interval[1])
            else:
                laste = interval[1]
        return count