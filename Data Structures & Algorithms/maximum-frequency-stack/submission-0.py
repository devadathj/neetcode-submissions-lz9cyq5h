class FreqStack:

    def __init__(self):
        self.counter = {}
        self.stacks = {}
        self.maxf = 0

    def push(self, val: int) -> None:
        count = 1 + self.counter.get(val, 0)
        if count > self.maxf:
            self.maxf = count
            self.stacks[self.maxf] = []

        self.stacks[count].append(val)
        self.counter[val] = count

    def pop(self) -> int:
        output = self.stacks[self.maxf].pop()
        self.counter[output] -= 1

        if len(self.stacks[self.maxf]) == 0:
            self.maxf -= 1
        
        return output


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()