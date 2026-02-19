1class Solution:
2    def longestBalanced(self, s: str) -> int:
3        n = len(s)
4        max_len = 0
5        for i in range(n):
6            freq = [0] * 26
7            distinct = 0
8            max_freq = 0
9            for j in range(i, n):
10                idx = ord(s[j]) - ord("a")
11                if freq[idx] == 0:
12                    distinct += 1
13
14                freq[idx] += 1
15
16                max_freq = max(max_freq, freq[idx])
17                
18                length = j - i + 1
19                if max_freq * distinct == length:
20                    max_len = max(max_len , length)
21        return max_len                