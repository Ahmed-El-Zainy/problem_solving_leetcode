1class Solution:
2    def repeatedStringMatch(self, a: str, b: str) -> int:
3        repeated = a
4        count = 1
5        while len(repeated) < len(b):
6            repeated += a
7            count +=1
8
9        if b in repeated:
10            return count
11
12        if b in repeated + a:
13            return count + 1
14        return -1