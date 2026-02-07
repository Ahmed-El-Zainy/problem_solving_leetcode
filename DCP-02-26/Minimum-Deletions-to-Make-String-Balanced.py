1class Solution:
2    def minimumDeletions(self, s: str) -> int:
3        s = s.replace("a", "0").replace("b", "1")
4        count_0 = s.count("0")
5        count_1 = 0
6        result = count_0
7        for c in s:
8            if c == "0":
9                count_0 -= 1
10            else:
11                count_1 += 1
12            result = min(result, count_0 + count_1)
13        return result
14