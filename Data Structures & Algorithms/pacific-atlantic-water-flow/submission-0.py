class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        reach_check = [[None] * COLS for _ in range(ROWS)]
        output = []

        def check_ocean(row, col, visited):
            print(str(row) +"____"+ str(col))
            if row < 0 or col < 0:
                return 'P'

            if row >= ROWS or col >= COLS:
                return 'A'

            if (row, col) in visited:
                return False

            visited.add((row, col))
            point_set = set()
            for i in directions:
                if 0 <= row + i[0] < ROWS and 0 <= col + i[1] < COLS:
                    if heights[row][col] < heights[row + i[0]][col + i[1]]:
                        point_set.add(False)
                    else:
                        if reach_check[row + i[0]][col + i[1]] is not None:
                            if reach_check[row + i[0]][col + i[1]] == True:
                                reach_check[row][col] = True
                                visited.remove((row, col))
                                return True
                            else:
                                point_set.add(reach_check[row + i[0]][col + i[1]])

                        elif reach_check[row + i[0]][col + i[1]] is None:

                            point_set.add(check_ocean(row + i[0], col + i[1], visited))
                else:
                    point_set.add(check_ocean(row + i[0], col + i[1], visited))
                
            if True in point_set or ('P' in point_set and 'A' in point_set):
                reach_check[row][col] = True
            elif 'P' in point_set:
                reach_check[row][col] = 'P'
            elif 'A' in point_set:
                reach_check[row][col] = 'A'
            else:
                reach_check[row][col] = False

            visited.remove((row, col))

            return reach_check[row][col]

        for i in range(ROWS):
            for j in range(COLS):
                if check_ocean(i, j, set()) == True:
                    output.append([i, j])
            
        return output
