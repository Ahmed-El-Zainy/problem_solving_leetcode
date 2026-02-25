1class Solution:
2    def sortByBits(self, arr: List[int]) -> List[int]:
3        
4        def count_ones(n):
5            count = 0
6            while n:
7                count += n & 1
8                n >>= 1
9            return count
10        
11        arr.sort(key=lambda x: (count_ones(x), x))
12        return arr