class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        ret_list = []
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
        
        highest = 0
        freqmap = [[] for _ in range(len(nums) + 1)]
        for key, value in hashmap.items():
            freqmap[value].append(key)
            if value > highest:
                highest = value

        for i in range(highest, -1, -1):
            for num in freqmap[i]:
                if k != 0:
                    ret_list.append(num)
                    k -= 1
                else:
                    return ret_list
        
        return ret_list
        


        
