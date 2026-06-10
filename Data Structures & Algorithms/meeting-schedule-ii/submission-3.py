"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if len(intervals) < 2:
            return len(intervals)

        intervals.sort(key=lambda x: (x.start, x.end))

        output = [intervals[0].end]

        for i in range(1, len(intervals)):
            
            for j in range(len(output)):
                if intervals[i].start >= output[j]:
                    output[j] = intervals[i].end
                    break
            else:
                output.append(intervals[i].end)

        return len(output)

        