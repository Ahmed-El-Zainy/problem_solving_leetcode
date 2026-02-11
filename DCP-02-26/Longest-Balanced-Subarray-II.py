1from typing import List
2
3class Node:
4    def __init__(self, x=None):
5        if x is None:
6            self.min = float('inf')
7            self.max = float('-inf')
8        else:
9            self.min = x
10            self.max = x
11        self.lazy = 0
12
13class SegmentTree:
14    def __init__(self, arr):
15        self.n = len(arr)
16        # 1-indexed segment tree with size 4*n
17        self.segTree = [Node() for _ in range(self.n * 4)]
18        self.build_tree(1, 0, self.n - 1, arr)
19    
20    def pull(self, i):
21        """Pull values from children up to parent"""
22        self.segTree[i].min = min(self.segTree[2*i].min, self.segTree[2*i+1].min)
23        self.segTree[i].max = max(self.segTree[2*i].max, self.segTree[2*i+1].max)
24    
25    def build_tree(self, i, l, r, arr):
26        if l == r:
27            self.segTree[i] = Node(arr[l])
28            return
29        
30        m = (l + r) >> 1
31        self.build_tree(2*i, l, m, arr)
32        self.build_tree(2*i+1, m+1, r, arr)
33        self.pull(i)
34    
35    def apply(self, i, l, r):
36        """Apply lazy propagation"""
37        if self.segTree[i].lazy == 0:
38            return
39        
40        self.segTree[i].min += self.segTree[i].lazy
41        self.segTree[i].max += self.segTree[i].lazy
42        
43        if l < r:
44            self.segTree[2*i].lazy += self.segTree[i].lazy
45            self.segTree[2*i+1].lazy += self.segTree[i].lazy
46        
47        self.segTree[i].lazy = 0
48    
49    def update_range(self, start, end, i, l, r, val):
50        """Range update with lazy propagation"""
51        self.apply(i, l, r)
52        
53        if l > end or r < start:
54            return
55        
56        if l >= start and r <= end:
57            self.segTree[i].lazy += val
58            self.apply(i, l, r)
59            return
60        
61        m = (l + r) >> 1
62        self.update_range(start, end, 2*i, l, m, val)
63        self.update_range(start, end, 2*i+1, m+1, r, val)
64        self.pull(i)
65    
66    def find_last_0(self, i, l, r):
67        """Find the last index where value is 0"""
68        self.apply(i, l, r)
69        
70        # If 0 isn't within [min, max], no 0 exists
71        if self.segTree[i].min > 0 or self.segTree[i].max < 0:
72            return -1
73        
74        if l == r:
75            return l
76        
77        m = (l + r) >> 1
78        # Search right child first to find the last 0
79        right = self.find_last_0(2*i+1, m+1, r)
80        if right != -1:
81            return right
82        return self.find_last_0(2*i, l, m)
83
84class Solution:
85    def longestBalanced(self, nums: List[int]) -> int:
86        n = len(nums)
87        
88        # For small inputs, use simpler O(n²) approach
89        if n <= 2000:
90            return self.longestBalanced_simple(nums)
91        
92        # Find maximum value to size the last array
93        M = max(nums)
94        last = [n] * (M + 1)
95        next_pos = [n] * n
96        
97        # Build next_pos array (next occurrence of same number)
98        for i in range(n - 1, -1, -1):
99            x = nums[i]
100            next_pos[i] = last[x]
101            last[x] = i
102        
103        # Compute prefix sums based on distinct odd/even counts
104        seen = set()
105        prefix = []
106        sum_val = 0
107        
108        for i in range(n):
109            x = nums[i]
110            if x not in seen:
111                # Odd numbers: +1, Even numbers: -1
112                sum_val += 1 if (x & 1) else -1
113                seen.add(x)
114            prefix.append(sum_val)
115        
116        # Build segment tree
117        seg = SegmentTree(prefix)
118        
119        # Initial answer: longest prefix with sum 0
120        ans = seg.find_last_0(1, 0, n - 1) + 1
121        
122        # Process each position
123        for i in range(n - 1):
124            r = next_pos[i] - 1
125            
126            # Update range when removing nums[i] from consideration
127            if i + 1 <= r:
128                # Reverse the contribution of nums[i]
129                val = -1 if (nums[i] & 1) else 1
130                seg.update_range(i + 1, r, 1, 0, n - 1, val)
131            
132            # Only search if better answer is possible
133            if i + ans + 1 < n:
134                right = seg.find_last_0(1, 0, n - 1)
135                if right != -1:
136                    ans = max(ans, right - i)
137        
138        return ans
139    
140    def longestBalanced_simple(self, nums: List[int]) -> int:
141        """Simple O(n²) solution for small inputs"""
142        n = len(nums)
143        max_len = 0
144        
145        for l in range(n):
146            if l > n - max_len:
147                break
148            
149            seen = set()
150            diff = 0
151            
152            for r in range(l, n):
153                x = nums[r]
154                if x not in seen:
155                    # Odd: +1, Even: -1
156                    diff += 1 if (x & 1) else -1
157                    seen.add(x)
158                
159                if diff == 0:
160                    max_len = max(max_len, r - l + 1)
161        
162        return max_len