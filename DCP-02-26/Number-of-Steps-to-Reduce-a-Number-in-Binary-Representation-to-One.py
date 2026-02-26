1class Solution:
2    def numSteps(self, s: str) -> int:
3        steps = 0
4        while s!= "1":
5            if s[-1] == "0":
6                s = s[:-1]
7            else:
8                s = bin(int(s, 2) + 1)[2:]
9            steps += 1
10        return steps
11
12    
13            