class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
            else:
                if temperatures[i - 1] >= temperatures[i]:
                    stack.append(i)
                else:
                    while stack and temperatures[stack[-1]] < temperatures[i]:
                        element = stack.pop()
                        diff = i - element
                        result[element] = diff
                    stack.append(i)
        
        return result



