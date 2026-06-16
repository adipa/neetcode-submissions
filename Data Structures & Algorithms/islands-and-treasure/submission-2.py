class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def addNext(r,c):
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                (r,c) in visited or
                grid[r][c] == -1):
                return
            q.append((r,c))
            visited.add((r,c))

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addNext(r+1, c)
                addNext(r-1, c)
                addNext(r, c+1)
                addNext(r, c-1)
            dist += 1




        