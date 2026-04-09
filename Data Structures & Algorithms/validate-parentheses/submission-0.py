class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_pair = {")" : "(", "}" : "{", "]" : "["}

        tracker = []

        for i in s:
            if i in bracket_pair:
                if len(tracker) > 0:
                    if bracket_pair[i] != tracker.pop():
                        return False
                else:
                    return False
            else:
                tracker.append(i)

        if len(tracker) == 0:
            return True
        else:
            return False