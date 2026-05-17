class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False

        all_nodes = set()

        node_list = {i:[] for i in range(n)}

        for edge in edges:
            node_list[edge[0]].append(edge[1])
            node_list[edge[1]].append(edge[0])

        def add_to_set(node):
            all_nodes.add(node)
            for i in node_list[node]:
                if i not in all_nodes:
                    add_to_set(i)
            
        add_to_set(0)

        return len(all_nodes) == n