1class Solution:
2    def hasAllCodes(self, s: str, k: int) -> bool:
3        seen = set()
4        for i in range(len(s) - k + 1):
5            seen.add(s[i: i+k])
6        return len(seen) == 2**k
7
8        # seen = set()
9        # for i in range(len(s) - k + 1):
10        #     seen.add(s[i:i+k])
11        # return len(seen) == 2**k