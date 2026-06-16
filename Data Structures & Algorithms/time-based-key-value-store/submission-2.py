class TimeMap:

    def __init__(self):
        self.master = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.master:
            self.master[key] = [(timestamp, value)]
        else:
            self.master[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.master:
            return ""

        low = 0
        high = len(self.master[key]) - 1

        output = ""
        while low <= high:
            mid = (low + high) // 2

            if self.master[key][mid][0] == timestamp:
                return self.master[key][mid][1]
            elif self.master[key][mid][0] > timestamp:
                high = mid - 1
            else:
                output = self.master[key][mid][1]
                low = mid + 1

        return output
