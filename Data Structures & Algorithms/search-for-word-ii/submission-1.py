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
            if "exist" in curr:
                res.append(curr["exist"])
                curr.pop("exist")
            
            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] not in curr or
                (r, c) in duplicate):
                return False
            
            for key, value in curr.items():
                if board[r][c] == key:
                    duplicate.add((r, c))
                    result = (dfs(r + 1, c, curr[key]) or
                        dfs(r - 1, c, curr[key]) or
                        dfs(r, c + 1, curr[key]) or
                        dfs(r, c - 1, curr[key]))
                    duplicate.remove((r, c))
            return result
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, hashmap)
        return res