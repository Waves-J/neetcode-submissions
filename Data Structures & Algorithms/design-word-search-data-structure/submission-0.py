class WordDictionary:

    def __init__(self):
        self.hashmap = {}

    def addWord(self, word: str) -> None:
        curr = self.hashmap

        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        
        curr["exist"] = True

        return

    def search(self, word: str) -> bool:

        def dfs(j, root):
            curr = root
            
            for i in range(j, len(word)):
                c = word[i]
                
                if c == ".":
                    for key, value in curr.items():
                        if key != "exist":
                            res = dfs(i + 1, value)
                            if res:
                                return res
                    return False
                    
                else:
                    if c not in curr:
                        return False
                    curr = curr[c]
                    
            return curr.get("exist", False)
            
        return dfs(0, self.hashmap)
