class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]

        i = 0
        list_len = len(intervals)

        while i < list_len:
            if newInterval[0] < intervals[i][0]:
                
                while i < list_len and newInterval[1] >= intervals[i][0]:
                    newInterval[1] = max(newInterval[1], intervals[i][1])
                    intervals.pop(i)
                    list_len -= 1

                if i > 0 and newInterval[0] <= intervals[i - 1][1]:
                    intervals[i - 1][1] = max(newInterval[1], intervals[i - 1][1])
                else:
                    intervals.insert(i, newInterval)

                return intervals
            
            i += 1
        
        if newInterval[0] <= intervals[-1][1]:
            intervals[-1][1] = max(newInterval[1], intervals[-1][1])
        else:
            intervals.append(newInterval)

        return intervals
            