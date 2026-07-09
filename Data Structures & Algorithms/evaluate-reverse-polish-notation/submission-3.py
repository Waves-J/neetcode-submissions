class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_list = ('+', '-', '*', '/')
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        for i in range(len(tokens)):
            if tokens[i] in op_list:
                num_right = stack.pop()
                num_left = stack.pop()
                op = tokens[i]
                if op == '+':
                    stack.append(num_left + num_right)
                elif op == '-':
                    stack.append(num_left - num_right)
                elif op == '*':
                    stack.append(num_left * num_right)
                else:
                    stack.append(int(num_left / num_right))
            else:
                stack.append(int(tokens[i]))
        
        return stack[0]



