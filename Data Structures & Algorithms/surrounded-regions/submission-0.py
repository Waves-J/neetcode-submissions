class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        safe = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            if ((r, c) in safe or
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                board[r][c] == "X"
            ):
                return
            
            safe.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        
        for r in range(1, ROWS - 1):
            dfs(r, 0)
            dfs(r, COLS - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in safe:
                    board[r][c] = "X"
        