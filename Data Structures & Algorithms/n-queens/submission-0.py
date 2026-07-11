class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        output = []

        def position_check(check, arr, row):
            if row >= n:
                output.append(arr.copy())
                return

            for j in range(n):
                if check[row][j]:
                    new_check = [x[:] for x in check]
                    update_check(new_check, row, j)
                    arr[row] = arr[row][:j] + "Q" + arr[row][j+1:]
                    position_check(new_check, arr, row + 1)
                    arr[row] = arr[row][:j] + "." + arr[row][j+1:]

        def update_check(check, row, col):

            for i in range(n):
                check[row][i] = False
                check[i][col] = False

            i, j = row, col
            while i >= 0 and j >= 0:
                check[i][j] = False
                i -= 1
                j -= 1

            i, j = row, col
            while i < n and j < n:
                check[i][j] = False
                i += 1
                j += 1

            i, j = row, col
            while i >= 0 and j < n:
                check[i][j] = False
                i -= 1
                j += 1

            i, j = row, col
            while i < n and j >= 0:
                check[i][j] = False
                i += 1
                j -= 1

            return check

        check = [[True] * n for _ in range(n)]
        arr = ["." * n for _ in range(n)]
        position_check(check, arr, 0)

        return output
