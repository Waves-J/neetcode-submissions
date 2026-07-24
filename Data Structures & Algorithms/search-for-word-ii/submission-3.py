class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            self.insert(word, trie)

        return self.exist(board, trie)
        
    def insert(self, word: str, hashmap: dict) -> None:
        curr = hashmap

        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        
        curr["exist"] = word

        return

    def exist(self, board: List[List[str]], hashmap: dict) -> bool:
        ROWS, COLS = len(board), len(board[0])
        duplicate = set()
        res = []

        def dfs(r, c, curr):
            # 1. Guard Clause (Bounds, Duplicates, and Trie validation)
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or 
                (r, c) in duplicate or board[r][c] not in curr):
                return

            # 2. Move to the exact node for this cell
            nextNode = curr[board[r][c]]

            # 3. Check if word exist
            if "exist" in nextNode:
                res.append(nextNode["exist"])
                nextNode.pop("exist") # Prevent duplicates
                
            # 4. Backtracking
            duplicate.add((r, c))

            dfs(r + 1, c, nextNode)
            dfs(r - 1, c, nextNode)
            dfs(r, c + 1, nextNode)
            dfs(r, c - 1, nextNode)

            duplicate.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, hashmap)
        return res