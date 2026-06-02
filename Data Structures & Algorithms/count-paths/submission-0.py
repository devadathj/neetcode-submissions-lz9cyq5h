class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        route_map = {}
        
        def path_count(i, j):

            if (i, j) in route_map:
                return route_map[(i, j)]

            if i >= m or j >= n:
                return 0

            if i == m - 1 and j == n - 1:
                return 1
                
            route_map[(i, j)] = path_count(i + 1, j) + path_count(i, j + 1)

            return route_map[(i, j)]

        return path_count(0, 0)

            