class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashdict = {}
        for num in nums:
            if not num in hashdict:
                hashdict[num] = [1, num]
                if num + 1 in hashdict and num - 1 in hashdict:
                    sizeleft = hashdict[hashdict[num - 1][1]][0]
                    sizeright = hashdict[hashdict[num + 1][1]][0]
                    if sizeleft > sizeright:
                        hashdict[num][1] = hashdict[num - 1][1]
                        hashdict[hashdict[num + 1][1]][1] = hashdict[num - 1][1]
                        hashdict[hashdict[num - 1][1]][0] += (sizeright + 1)
                    else:
                        hashdict[num][1] = hashdict[num + 1][1]
                        hashdict[hashdict[num - 1][1]][1] = hashdict[num + 1][1]
                        hashdict[hashdict[num + 1][1]][0] += (sizeleft + 1)

                elif num + 1 in hashdict:
                    hashdict[num][1] = hashdict[num + 1][1]
                    hashdict[hashdict[num][1]][0] += 1
                elif num - 1 in hashdict:
                    hashdict[num][1] = hashdict[num - 1][1]
                    hashdict[hashdict[num][1]][0] += 1
           
        longest = 0
        for key, value in hashdict.items():
            if value[0] > longest:
                longest = value[0]

        return longest
