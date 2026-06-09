class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x: x[0])

        output = []

        for i in range(len(intervals) - 1):

            if intervals[i][1] < intervals[i + 1][0]:
                output.append(intervals[i])
            else:
                intervals[i + 1] = [min(intervals[i][0], intervals[i + 1][0]), max(intervals[i][1], intervals[i + 1][1])]

        output.append(intervals[i + 1])

        return output
