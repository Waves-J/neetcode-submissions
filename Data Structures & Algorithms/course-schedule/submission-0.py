class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        linked = {}
        self.isCycle = False
        gray = set()
        black = set()
        
        for i in range(numCourses):
            linked[i] = set()
        for prereq in prerequisites:
            linked[prereq[1]].add(prereq[0])

        def dfs(v):
            if v in black:
                return

            gray.add(v)
            for prereq in linked[v]:
                if prereq in gray:
                    self.isCycle = True
                elif prereq not in black:
                    dfs(prereq)
            
            gray.remove(v)
            black.add(v)

        for prereq in prerequisites:
            dfs(prereq[1])
        
        return not self.isCycle
