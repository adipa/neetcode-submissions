class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0

        def addNext(r,c):
            nonlocal fresh
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                grid[r][c] != 1):
                return
            q.append((r,c))
            grid[r][c] = 2
            fresh -= 1

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        # visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    # visited.add((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                addNext(r+1, c)
                addNext(r-1, c)
                addNext(r, c+1)
                addNext(r, c-1)
            minutes += 1

        return minutes if not fresh else -1

        