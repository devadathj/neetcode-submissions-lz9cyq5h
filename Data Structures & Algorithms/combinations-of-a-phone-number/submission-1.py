class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        num_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        output = []
        arr = []

        def make_string(i):
            if len(arr) == len(digits):
                output.append("".join(arr))
                return

            for j in num_map[digits[i]]:
                arr.append(j)
                make_string(i + 1)
                arr.pop()

        make_string(0)
        return output

