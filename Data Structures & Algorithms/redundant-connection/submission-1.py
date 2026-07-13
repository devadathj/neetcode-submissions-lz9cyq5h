class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parents = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find_parent(i):
            if i != parents[i]:
                parents[i] = find_parent(parents[i])

            return parents[i]

        def check_parents(i, j):
            p1, p2 = find_parent(i), find_parent(j)
            if p1 == p2:
                return False

            if rank[p1] < rank[p2]:
                parents[p1] = parents[p2]
                rank[p2] += rank[p1]
            else:
                parents[p2] = parents[p1] 
                rank[p1] += rank[p2]
            return True

        for edge in edges:
            if not check_parents(edge[0], edge[1]):
                return edge

            
