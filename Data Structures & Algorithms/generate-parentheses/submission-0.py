class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        output = []

        arr = ['(']
        l = 1
        r = 0

        def create_str(curr, l, r):

            if len(curr) == 2 * n:
                output.append("".join(curr))
                return

            if r > l:
                return

            if l < n:
                curr.append('(')
                create_str(curr, l + 1, r)
                curr.pop()

            if r < n and r < l:
                curr.append(')')
                create_str(curr, l, r + 1)
                curr.pop()

        create_str(arr, l, r)
        return output


