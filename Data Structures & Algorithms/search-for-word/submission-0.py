class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(i, j, k):
            if k == len(word):
                return True
            
            if (i < 0 or
                j < 0 or
                i >= rows or
                j >= cols or
                board[i][j] != word[k]):
                return False

            temp, board[i][j] = board[i][j] , '#'

            result = (dfs(i+1, j, k + 1) or
                        dfs(i-1, j, k + 1) or
                        dfs(i, j-1, k + 1) or
                        dfs(i, j+1, k + 1))

            board[i][j] = temp
            return result
                        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False
            

        