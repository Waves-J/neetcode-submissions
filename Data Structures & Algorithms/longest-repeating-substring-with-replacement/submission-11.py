class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        most_amt = 0
        window_char = defaultdict(int)
        most_char = ""

        left = 0
        right = 0

        while right < len(s):
            window_char[s[right]] += 1
            if window_char[s[right]] > window_char[most_char]:
                most_char = s[right]

            if window_char[most_char] + k > right - left:
                most_amt += 1
                right += 1
            else:
                window_char[s[left]] -= 1
                left += 1
                right += 1
                
                for key in window_char:
                    if window_char[key] > window_char[most_char]:
                        most_char = key
                
        
        return most_amt
            




            