class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        part = []
        hashmap = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
                    "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
                    "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        
        def backtrack(i):
            if i == len(digits):
                if part:
                    result.append("".join(part))
                return
            
            for letter in hashmap[digits[i]]:
                part.append(letter)
                backtrack(i + 1)
                part.pop()

        backtrack(0)
        return result
        



        