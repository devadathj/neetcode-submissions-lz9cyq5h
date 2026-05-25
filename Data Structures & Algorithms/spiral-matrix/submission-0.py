class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        output = []

        r, c = 0, 0
        cur_entries, tot_entries = 0, len(matrix) * len(matrix[0])  

        while True:
            for c in range(left, right + 1):
                output.append(matrix[r][c])
                cur_entries += 1
            if cur_entries == tot_entries:
                break
            top += 1

            for r in range(top, bottom + 1):
                output.append(matrix[r][c])
                cur_entries += 1
            if cur_entries == tot_entries:
                break
            right -= 1

            for c in range(right, left - 1, -1):
                output.append(matrix[r][c])
                cur_entries += 1
            if cur_entries == tot_entries:
                break
            bottom -= 1

            for r in range(bottom, top - 1, -1):
                output.append(matrix[r][c])
                cur_entries += 1
            if cur_entries == tot_entries:
                break
            left += 1

        return output