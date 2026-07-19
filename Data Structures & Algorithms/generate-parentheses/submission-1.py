class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        def backtrack(open_count, closed_count):
            
            # Base Case:
            if open_count == closed_count == n:
                res.append("".join(stack))
                return

            # Decision 1
            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, closed_count)
                stack.pop() # Backtrack

            # Decision 2
            if closed_count < open_count:
                stack.append(")")
                backtrack(open_count, closed_count + 1)
                stack.pop() # Backtrack
                
        backtrack(0, 0)
        return res