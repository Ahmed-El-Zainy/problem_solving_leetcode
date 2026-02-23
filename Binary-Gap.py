1class Solution:
2    def binaryGap(self, n: int) -> int:
3        # Convert n to binary string
4        binary_str = bin(n)[2:]  # Remove '0b' prefix
5        
6        max_gap = 0
7        last_one_index = None
8        
9        for i, bit in enumerate(binary_str):
10            if bit == '1':
11                if last_one_index is not None:
12                    gap = i - last_one_index
13                    max_gap = max(max_gap, gap)
14                last_one_index = i
15        
16        return max_gap