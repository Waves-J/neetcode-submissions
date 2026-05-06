class Solution:

    def encode(self, strs: List[str]) -> str:
        rstr = []
        for s in strs:
            rstr.append(str(len(s)))
            rstr.append("#")
            rstr.append(s)
        return "".join(rstr)

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
                curr_str = s[i:i + int(curr_len)]
                i += int(curr_len)
                rlist.append(curr_str)
                curr_len = ""
                curr_str = ""
        
        return rlist


