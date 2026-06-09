class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: (x[0], x[1]))

        output = 0

        last_y = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < last_y:
                output += 1
                last_y = min(last_y, intervals[i][1])
            else:
                last_y = intervals[i][1]

        return output