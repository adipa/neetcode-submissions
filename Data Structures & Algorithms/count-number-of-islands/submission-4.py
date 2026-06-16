class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set() # tuple of indices visited
        neighbors = [[1,0], [-1,0], [0, 1], [0, -1]]

        def markSameIsland(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                for nr, nc in neighbors:
                    tr = row + nr
                    tc = col + nc

                    if (tr in range(rows) and
                        tc in range(cols) and
                        grid[tr][tc] == "1" and
                        (tr, tc) not in visited):

                        q.append((tr,tc))
                        visited.add((tr,tc))

        def markSameIslandDFS(r,c):
            visited.add((r,c))

            for nr, nc in neighbors:
                tr = r + nr
                tc = c + nc

                if (tr in range(rows) and
                    tc in range(cols) and
                    grid[tr][tc] == "1" and
                    (tr, tc) not in visited):

                    markSameIslandDFS(tr,tc)             

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    markSameIslandDFS(r,c)
                    islands += 1
        return islands
        