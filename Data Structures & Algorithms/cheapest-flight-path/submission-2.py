class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        flight_map = defaultdict(list)

        for from_city, to_city, price in flights:
            flight_map[from_city].append((to_city, price))

        price_to_city = [float('inf')] * n
        price_to_city[src] = 0

        route_check = deque()
        route_check.append(src)

        for _ in range(k + 1):
            new_prices = price_to_city.copy()
            for iterq in range(len(route_check)):

                cur_city = route_check.popleft()
                
                for to_city, price in flight_map[cur_city]:
                    if price_to_city[cur_city] + price < new_prices[to_city]:
                        new_prices[to_city] = price_to_city[cur_city] + price
                        route_check.append(to_city)

            price_to_city = new_prices

        return price_to_city[dst] if price_to_city[dst] != float('inf') else -1