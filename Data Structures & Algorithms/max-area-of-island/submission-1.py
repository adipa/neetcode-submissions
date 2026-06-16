class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        neighbors = [[1,0], [-1,0], [0, 1], [0, -1]]

        def calArea(r,c):
            area = 1
            grid[r][c] = "0"

            for nr, nc in neighbors:
                tr = r + nr
                tc = c + nc

                if (tr in range(ROWS) and
                    tc in range(COLS) and
                    grid[tr][tc] == 1):

                    area += calArea(tr,tc)

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(calArea(r, c), maxArea)
        return maxArea