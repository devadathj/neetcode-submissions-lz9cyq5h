"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if len(intervals) < 2:
            return len(intervals)

        intervals.sort(key=lambda x: (x.start, x.end))
        output = [intervals[0].end]
        for i in range(1, len(intervals)):
            
            if intervals[i].start >= output[0]:
                heapq.heappop(output)
            heapq.heappush(output, intervals[i].end)

        return len(output)

        