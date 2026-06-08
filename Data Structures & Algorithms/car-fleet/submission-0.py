class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posdec = []
        for i in range(len(position)):
            posdec.append([position[i], speed[i]])
        
        posdec.sort()
        
        stack = []
        for i in range(len(position) - 1, -1, -1):
            time = (target - posdec[i][0]) / posdec[i][1]
            if not stack:
                stack.append(time)
            else:
                if time > stack[-1]:
                    stack.append(time)
        
        return len(stack)


