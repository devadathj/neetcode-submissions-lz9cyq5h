import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        tracker = []

        for point in points:
            
            dist = ((point[0] ** 2) + (point[1] **2)) ** 0.5

            heapq.heappush_max(tracker, (dist, point))

            if len(tracker) > k:
                heapq.heappop_max(tracker)

        output = []
        for i in tracker:
            output.append(i[1])

        return output