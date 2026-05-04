class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        ret_list = []
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        freqmap = [[] for _ in range(len(nums) + 1)]

        for key, value in hashmap.items():
            freqmap[value].append(key)

        for i in range(len(freqmap) - 1, 0, -1):
            for num in freqmap[i]:
                ret_list.append(num)
                if len(ret_list) == k:
                    return ret_list
        
        return ret_list
        


        
