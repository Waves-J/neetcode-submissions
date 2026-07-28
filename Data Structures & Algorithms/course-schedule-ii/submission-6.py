class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        linked = {}
        self.isCycle = False
        order = []
        gray = set()
        black = set()
        
        for i in range(numCourses):
            linked[i] = []
        for prereq in prerequisites:
            linked[prereq[1]].append(prereq[0])

        def dfs(v):
            if v in black or self.isCycle:
                return

            gray.add(v)
            for prereq in linked[v]:
                if prereq in gray:
                    self.isCycle = True
                    return
                elif prereq not in black:
                    dfs(prereq)
            
            gray.remove(v)
            order.append(v)
            black.add(v)
        
        for i in range(numCourses):
            dfs(i)
        
        order.reverse()
        return order if not self.isCycle else []
