class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket = {'(', '{', '['}
        stack = []

        for i in range(len(s)):
            if s[i] in open_bracket:
                stack.append(s[i])
            else:
                if s[i] == ')' and len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                elif s[i] == '}' and len(stack) > 0 and stack[-1] == '{':
                    stack.pop()
                elif s[i] == ']'  and len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        
        return True
        
