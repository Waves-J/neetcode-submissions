class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        self.curr = 0
        used = set()
        candidates.sort()

        def backtrack(starting_index):
            if self.curr < target:
                for k in range(starting_index, len(candidates)):
                    if candidates[k] == candidates[k-1] and k > starting_index: continue
                    self.curr += candidates[k]
                    subset.append(candidates[k])
                    backtrack(k + 1)
                    self.curr -= subset.pop()

            elif self.curr == target:
                result.append(subset[:])

        backtrack(0)
        return result      