class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        left = 0
        right = 0

        hashmap = defaultdict(int)
        hashmaptwo = defaultdict(int)

        for char in s1:
            hashmap[char] += 1

        while right < len(s1):
            if s2[right] in hashmap:
                hashmaptwo[s2[right]] += 1
            right += 1
        
        right -= 1

        while right < len(s2):
            if hashmap == hashmaptwo:
                return True
            
            right += 1
            if right < len(s2) and s2[right] in hashmap:
                hashmaptwo[s2[right]] += 1
            if s2[left] in hashmap:
                hashmaptwo[s2[left]] -= 1

            left += 1
    
        return False
                

            


