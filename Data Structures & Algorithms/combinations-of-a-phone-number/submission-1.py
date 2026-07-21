class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        part = []
        hashmap = {"2": "abc", "3": "def", "4": "ghi",
                    "5": "jkl", "6": "mno", "7": "pqrs",
                    "8": "tuv", "9": "wxyz"}
        
        def backtrack(i):
            if i == len(digits):
                result.append("".join(part))
                return
            
            for letter in hashmap[digits[i]]:
                part.append(letter)
                backtrack(i + 1)
                part.pop()

        backtrack(0)
        return result
        



        