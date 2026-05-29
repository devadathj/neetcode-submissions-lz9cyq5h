class Solution:
    def numDecodings(self, s: str) -> int:
        
        s_len = len(s)
        combo_count = {s_len: 1}

        def sub_anal(i):
            if i in combo_count:
                return combo_count[i]

            if s[i] == '0':
                return 0
            
            result = sub_anal(i + 1)

            if i + 1 < s_len and (s[i] == "1" or  (s[i] == "2" and s[i + 1] < "7")):
                result += sub_anal(i + 2)
            combo_count[i] = result

            return result

        return sub_anal(0)
