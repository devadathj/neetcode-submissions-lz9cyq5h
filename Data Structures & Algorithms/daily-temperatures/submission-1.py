from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = deque()
        result.appendleft(0)

        tracker = deque()
        tracker.append(len(temperatures) - 1)

        for i in range(len(temperatures) - 2, -1, -1):
            while tracker and temperatures[i] >= temperatures[tracker[-1]]:
                tracker.pop()

            if tracker:
                result.appendleft(tracker[-1] - i)
            else:
                result.appendleft(0)

            tracker.append(i)
        
        return list(result)

