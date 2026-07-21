class PrefixTree:

    def __init__(self):
        self.hashmap = {}

    def insert(self, word: str) -> None:
        curr = self.hashmap

        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        
        curr["exist"] = True

        return
            
    def search(self, word: str) -> bool:
        curr = self.hashmap

        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        
        if "exist" in curr:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.hashmap

        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]
        
        return True
        