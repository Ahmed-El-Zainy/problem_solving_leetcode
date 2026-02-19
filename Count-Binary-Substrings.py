1class Solution:
2    def countBinarySubstrings(self, s: str) -> int:
3        prev = 0
4        count = 1
5        result = 0
6        for i in range(1, len(s)):
7            if s[i] == s[i - 1]:
8                count += 1
9            else:
10                result += min(prev, count)
11                prev = count
12                count = 1
13        result += min(prev, count)
14        return result