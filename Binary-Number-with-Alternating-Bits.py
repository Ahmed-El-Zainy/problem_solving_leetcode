1class Solution:
2    def hasAlternatingBits(self, n: int) -> bool:
3        prev = n & 1
4        n >>= 1
5        while n:
6            curr = n & 1
7            if curr == prev:
8                return False
9            prev = curr
10            n >>= 1
11        return True