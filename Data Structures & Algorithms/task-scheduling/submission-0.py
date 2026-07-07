import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counter = {}

        for char in tasks:
            counter[char] = counter.get(char, 0) + 1

        max_heap = [] 

        for _, val in counter.items():
            heapq.heappush_max(max_heap, val)

        q = deque()
        output = 0
        while max_heap or q:
            output += 1

            if max_heap:
                task = heapq.heappop_max(max_heap) - 1
                if task:
                    q.append((task, output + n))

            if q and q[0][1] == output:
                heapq.heappush_max(max_heap, q.popleft()[0])

        return output

        