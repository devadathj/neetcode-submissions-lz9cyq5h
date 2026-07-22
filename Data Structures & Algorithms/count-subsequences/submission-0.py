class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        tracker = {}

        def check_seq(indexs, indext):
            if indexs >= len(s):
                return 0

            if (indexs, indext) in tracker:
                return tracker[(indexs, indext)]
            
            tracker[(indexs, indext)] = 0
            if s[indexs] != t[indext]:
                tracker[(indexs, indext)] += check_seq(indexs + 1, indext)

            elif s[indexs] == t[indext]:
                if indext == len(t) - 1:
                    tracker[(indexs, indext)] += 1 + check_seq(indexs + 1, indext)
                else:
                    tracker[(indexs, indext)] += check_seq(indexs + 1, indext + 1) + check_seq(indexs + 1, indext)

            return tracker[(indexs, indext)]

        return check_seq(0, 0)