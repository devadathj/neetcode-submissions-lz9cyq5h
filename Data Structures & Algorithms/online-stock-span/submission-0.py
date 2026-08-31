class StockSpanner:

    def __init__(self):
        self.series = []

    def next(self, price: int) -> int:
        span = 1
        while self.series and self.series[-1][0] <= price:
            span += self.series[-1][1]
            self.series.pop()

        self.series.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)