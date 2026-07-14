class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_map = {}
        for i in range(1, n + 1):
            adj_map[i] = []

        for start, end, time in times:
            adj_map[start].append((end, time))

        min_times = [float('inf')] * (n + 1)
        min_times[0] = -1

        q = [(0, k)]
        visited = set()
        while q:
            curr_time, curr_node = heapq.heappop(q)

            if curr_node not in visited:
                min_times[curr_node] = curr_time
                visited.add(curr_node)
                
                for end, time in adj_map[curr_node]:
                    if end not in visited:
                        heapq.heappush(q, (curr_time + time, end))

        output = max(min_times)

        return output if output != float("inf") else -1

