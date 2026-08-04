class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        counter = {}

        for i, letter in enumerate(s):
            if letter not in counter:
                counter[letter] = [i, i]
            else:
                counter[letter][1] = i

        output = []
        last_loc = -1

        for val in counter.values():
            if val[0] > last_loc:
                output.append(val[1] - val[0] + 1)
                last_loc = val[1]
            else:
                if val[1] > last_loc:
                    output[-1] += val[1] - last_loc
                    last_loc = val[1]

        return output