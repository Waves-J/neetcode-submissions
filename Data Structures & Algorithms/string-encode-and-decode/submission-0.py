class Solution:

    def encode(self, strs: List[str]) -> str:
        rstr = ""
        for s in strs:
            rstr += str(len(s))
            rstr += "#"
            rstr += s
        return rstr

    def decode(self, s: str) -> List[str]:
        curr_len = ""
        curr_str = ""
        rlist = []
        i = 0
        while i < len(s):
            if s[i] != "#":
                curr_len += s[i]
                i += 1
            else:
                i += 1
                for j in range(int(curr_len)):
                    curr_str += s[i]
                    i += 1
                rlist.append(curr_str)
                curr_len = ""
                curr_str = ""
        
        return rlist


