1class Solution:
2    def addBinary(self, a: str, b: str) -> str:
3        carry = 0
4        res = []
5        i, j = len(a) - 1, len(b) - 1
6        while i >= 0 or j >= 0 or carry:
7            x = int(a[i]) if i >= 0 else 0
8            y = int(b[j]) if j >= 0 else 0
9            s = x + y + carry
10            res.append(str(s % 2))
11            carry = s // 2
12            i -= 1
13            j -= 1
14
15        return ''.join(reversed(res))