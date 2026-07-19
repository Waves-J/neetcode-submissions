class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(string, opening, closing):
            if closing == 0 and opening == 0:
                result.append(string)
                return
            
            if opening > 0:
                substr = string + "("
                backtrack(substr, opening - 1, closing)
            
            if closing > 0 and closing - 1 >= opening:
                substr = string + ")"
                backtrack(substr, opening, closing - 1)
            
        backtrack("", n, n)
        return result