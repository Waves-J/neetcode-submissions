class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)

        longest = 0
        
        for num in hashset:
            count = 1
            if not num - 1 in hashset:
                for i in range(1, len(nums)):
                    if num + i in hashset:
                        count += 1
                    else:
                        break
                
                if count > longest:
                    longest = count

        return longest
