class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def row_search(low, high, row):
            if low > high:
                return False

            mid = (low + high) // 2

            if matrix[row][mid] > target:
                return row_search(low, mid - 1, row)
            elif matrix[row][mid] == target:
                return True
            else:
                return row_search(mid + 1, high, row)

        def col_search(low, high):
            if low > high:
                return False

            mid = (low + high) // 2

            if matrix[mid][0] == target or matrix[mid][-1] == target:
                return True
            elif matrix[mid][0] < target < matrix[mid][-1]:
                return row_search(0, len(matrix[mid]) - 1, mid)
            elif matrix[mid][0] > target:
                return col_search(low, mid - 1)
            elif matrix[mid][-1] < target:
                return col_search(mid + 1, high)

        return col_search(0, len(matrix) - 1)