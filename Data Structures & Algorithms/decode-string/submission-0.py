class Solution:
    def decodeString(self, s: str) -> str:
        
        self.index = 0

        def unpack():
            result = ""
            num = 0

            while self.index < len(s):
                c = s[self.index]
                if c.isdigit():
                    num = num * 10 + int(c)
                elif c == "[":
                    self.index += 1
                    result += num * unpack()
                    num = 0
                elif c == "]":
                    return result
                else:
                    result += c

                self.index += 1

            return result

        return unpack()

