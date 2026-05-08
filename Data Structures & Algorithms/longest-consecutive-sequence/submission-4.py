class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        seq = set()

        longest = 0
        
        for num in hashset:
            count = 1
            if not num in seq and not num - 1 in hashset:
                seq.add(num)
                for i in range(1, len(nums) - len(seq) + 1):
                    if num + i in hashset:
                        count += 1
                        seq.add(num + i)
                    else:
                        break
                
                if count > longest:
                    longest = count

        return longest
