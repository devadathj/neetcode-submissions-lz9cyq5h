class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances = []
        output = 0
        output_edges = 0

        rank = [1] * len(points)
        parent = [i for i in range(len(points))]

        def cal_dist(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parentx = find(x)
            parenty = find(y)

            if parentx == parenty:
                return False

            if rank[parentx] < rank[parenty]:
                rank[parentx] += rank[parenty]
                parent[parentx] = parent[parenty]
            else:
                rank[parentx] += rank[parenty]
                parent[parenty] = parent[parentx]

            return True


        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                heapq.heappush(distances, (cal_dist(points[i], points[j]), i, j))
        
        while distances and output_edges < len(points) - 1:
    
            curr_dist, point1, point2 = heapq.heappop(distances)

            if union(point1, point2):
                output += curr_dist
                output_edges += 1  

        return output