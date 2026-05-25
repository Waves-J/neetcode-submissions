class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        hashmap = defaultdict(int)

        for c in t:
            hashmap[c] += 1
        
        left = 0
        right = 0
        minsub = (-1, -1)
        minlen = len(s) + 1

        for right in range(len(s)):
            if s[right] in hashmap:
                hashmap[s[right]] -= 1
            
            while all(val <= 0 for val in hashmap.values()):
                if minlen > (right - left + 1):
                    minlen = right - left + 1
                    minsub = (left, right)
                    
                if s[left] in hashmap:
                    hashmap[s[left]] += 1
                left += 1
        
        return s[minsub[0]: minsub[1] + 1]



            

