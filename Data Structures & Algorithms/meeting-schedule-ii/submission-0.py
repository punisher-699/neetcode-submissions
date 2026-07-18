"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        if len(intervals) == 1: return 1
        intervals.sort(key = lambda x: x.start)
        rooms = 0
        prev = intervals[0].end

        for interval in intervals[1:]:
            if interval.start < prev:
                prev = max(prev, interval.end)
                rooms += 1
            else:
                prev = interval.end
        return rooms
            


        