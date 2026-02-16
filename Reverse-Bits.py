1class Solution:
2    def reverseBits(self, n: int) -> int:
3        result = 0
4        for i in range(32):
5            result = (result << 1) | (n & 1)
6            n >>= 1
7        return result