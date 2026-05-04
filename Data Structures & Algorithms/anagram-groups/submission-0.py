class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        return_list = []
        for i in range(len(strs)):
            sorted_text = "".join(sorted(strs[i]))
            if sorted_text in hashmap:
                return_list[hashmap[sorted_text]].append(strs[i])
            else:
                return_list.append([strs[i]])
                hashmap[sorted_text] = len(return_list) - 1
        
        return return_list