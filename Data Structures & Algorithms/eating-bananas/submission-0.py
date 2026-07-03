class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        most = max(piles)

        i = 1
        j = most
        k = most

        while i <= j:
            m = (j + i) // 2
            curr_h = 0
            for num in range(len(piles)):
                curr_h += math.ceil(piles[num] / m)

            if curr_h > h:
                i = m + 1
            else:
                j = m - 1
                if m < k:
                    k = m

        return k

