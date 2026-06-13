class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = [float("inf")]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.stack_min.append(min(self.stack_min[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.stack_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]
