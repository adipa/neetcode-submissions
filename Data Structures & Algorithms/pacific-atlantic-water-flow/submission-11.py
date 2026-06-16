from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        ROWS, COLS = len(heights), len(heights[0])
        pacific_visited = [[False] * COLS for _ in range(ROWS)]
        atlantic_visited = [[False] * COLS for _ in range(ROWS)]
        
        def dfs(r, c, visited, prev_height):
            # Boundary and height check
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or 
                visited[r][c] or heights[r][c] < prev_height):
                return
            visited[r][c] = True
            
            # Recursive DFS on all four directions
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # Run DFS from all Pacific border cells
        for c in range(COLS):
            dfs(0, c, pacific_visited, heights[0][c])       # Top edge (Pacific)
            dfs(ROWS - 1, c, atlantic_visited, heights[ROWS - 1][c])  # Bottom edge (Atlantic)
        for r in range(ROWS):
            dfs(r, 0, pacific_visited, heights[r][0])       # Left edge (Pacific)
            dfs(r, COLS - 1, atlantic_visited, heights[r][COLS - 1])  # Right edge (Atlantic)

        # Collect cells that can reach both oceans
        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if pacific_visited[r][c] and atlantic_visited[r][c]:
                    result.append([r, c])
                    
        return result
