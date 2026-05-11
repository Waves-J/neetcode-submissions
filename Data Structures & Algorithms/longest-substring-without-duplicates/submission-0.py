class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        longest = 0
        duplicated = set()

        while right < len(s):
            if s[right] not in duplicated:
                duplicated.add(s[right])
                longest = max(longest, len(duplicated))
                right += 1
            else:  
                duplicated.remove(s[left])
                left += 1

        return longest
            

