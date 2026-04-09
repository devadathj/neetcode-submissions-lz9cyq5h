from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_dict = dict()

        for x in t:
            t_dict[x] = t_dict.get(x, 0) + 1

        locations = defaultdict(list)
        output_length = 9999
        output = ""

        left = 0
        for right in range(len(s)):
            if s[right] in t_dict.keys():
                locations[s[right]].append(right)

                if s[right] in locations.keys():
                    if len(locations[s[right]]) > t_dict[s[right]]: 
                        locations[s[right]].remove(min(locations[s[right]]))
                    if len(locations[s[right]]) == t_dict[s[right]]: 
                        left = min(min(x) for x in locations.values())
                        
                if sum(len(x) for x in locations.values()) == len(t) and output_length > right - left:
                    output_length = right - left
                    output = s[left : right + 1]

        return output
