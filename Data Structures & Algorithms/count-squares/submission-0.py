class CountSquares:

    def __init__(self):
        self.points_map = {}

    def add(self, point: List[int]) -> None:
        self.points_map[tuple(point)] = self.points_map.get(tuple(point), 0) + 1

    def count(self, point: List[int]) -> int:
        count = 0

        for p in self.points_map.keys():
            if p[0] != point[0] and p[1] != point[1]:
                if (p[0], point[1]) in self.points_map and (point[0], p[1]) in self.points_map:
                    count += self.points_map[p] * self.points_map[(p[0], point[1])] * self.points_map[(point[0], p[1])]

        return count
