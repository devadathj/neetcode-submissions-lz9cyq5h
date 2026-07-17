class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        tickets.sort(reverse=True)

        adj_map = {}
        for start, end in tickets:
            if start not in adj_map:
                adj_map[start] = []
            adj_map[start].append(end)

        output = []

        def make_route(start):
            if start in adj_map:
                while adj_map[start]:
                    end = adj_map[start].pop()
                    make_route(end)
            output.append(start)

        make_route("JFK")
        return output[::-1]