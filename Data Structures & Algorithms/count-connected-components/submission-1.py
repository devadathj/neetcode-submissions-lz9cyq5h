class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        node_list = {i:[] for i in range(n)}

        for edge in edges:
            node_list[edge[0]].append(edge[1])
            node_list[edge[1]].append(edge[0])

        num_sets = [set()]
        visited = set()

        def add_nodes(node):
            if node in visited:
                return
            
            visited.add(node)
            num_sets[-1].add(node)
            for neighbor in node_list[node]:
                if neighbor not in num_sets[-1]:
                    add_nodes(neighbor)

        add_nodes(0)
        for i in range(n):
            if i not in visited:
                num_sets.append(set())
                add_nodes(i)

        return len(num_sets)