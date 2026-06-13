class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        track = []

        for i in tokens:
            if i == "+":
                track.append(track.pop() + track.pop())
            elif i == "-":
                track.append(0 - track.pop() + track.pop())
            elif i == "*":
                track.append(track.pop() * track.pop())
            elif i == "/":
                track.append(int(1 / track.pop() * track.pop()))
            else:
                track.append(int(i))

        return track.pop()