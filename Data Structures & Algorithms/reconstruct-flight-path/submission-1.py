class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        tickets.sort()

        adj_map = {}
        for start, end in tickets:
            if start not in adj_map:
                adj_map[start] = []
            adj_map[start].append(end)

        output = ["JFK"]

        def make_route(start):
            if len(output) == len(tickets) + 1:
                return True

            if start not in adj_map:
                return False

            temp = adj_map[start].copy()

            for i, end in enumerate(temp):
                adj_map[start].pop(i)
                output.append(end)

                if make_route(end):
                    return True

                adj_map[start].insert(i, end)
                output.pop()

            return False

        make_route("JFK")
        return output