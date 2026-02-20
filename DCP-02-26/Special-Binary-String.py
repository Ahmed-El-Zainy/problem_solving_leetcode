1class Solution:
2    def makeLargestSpecial(self, s: str) -> str:
3        # A special binary string:
4        # 1. Equal number of 0s and 1s
5        # 2. Every prefix has >= as many 1s as 0s
6        # (Same structure as valid parentheses: 1='(' 0=')')
7        
8        # Strategy: Find top-level special substrings, recursively
9        # sort their insides, then sort them in descending order
10        
11        count = 0
12        start = 0
13        specials = []
14        
15        for i, ch in enumerate(s):
16            if ch == '1':
17                count += 1
18            else:
19                count -= 1
20            
21            if count == 0:
22                # s[start:i+1] is a top-level special string
23                # Recursively optimize the inside (strip outer 1 and 0)
24                inner = self.makeLargestSpecial(s[start+1:i])
25                specials.append('1' + inner + '0')
26                start = i + 1
27        
28        # Sort descending so largest special strings come first
29        specials.sort(reverse=True)
30        return ''.join(specials)