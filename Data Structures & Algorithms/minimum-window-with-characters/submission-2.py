class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_dict = dict()
        for x in t:
            t_dict[x] = t_dict.get(x, 0) + 1
        
        output = ""
        output_length = 9999
        need = len(t_dict)
        have = 0

        locations = dict()
        left = 0
        for right in range(len(s)):
            if s[right] in t_dict.keys():
                locations[s[right]] = locations.get(s[right], 0) + 1

                if locations[s[right]] == t_dict[s[right]]:
                    have += 1
                
                while have == need:
                    if output_length > right - left + 1:
                        output_length = right - left + 1
                        output = s[left : right + 1]

                    if s[left] in t_dict:
                        locations[s[left]] -= 1

                        if locations[s[left]] < t_dict[s[left]]:
                            have -= 1
                    
                    left += 1
              
        return output
