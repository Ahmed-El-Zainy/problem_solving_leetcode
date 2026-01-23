1class Solution:
2    def minimumPairRemoval(self, l: List[int]) -> int:
3        n = len(l)
4        l.append(inf)  # Sentinel value to simplify edge handling
5        le, ri = list(range(-1, n)), list(range(1, n + 1))  # Doubly linked list simulation
6        h = [(a + b, i) for i, (a, b) in enumerate(pairwise(l))]  # Min-heap of (sum, index)
7        heapify(h)
8
9        ans = 0  # Operation count
10        rest = n - sum(1 for a, b in pairwise(l) if a <= b)  # Count of violating pairs
11
12        while rest > 0:
13            v, i = heappop(h)
14            r = ri[i]
15            # Skip if this pair is outdated
16            if le[r] != i or l[i] + l[r] != v:
17                continue
18
19            rr = ri[r]
20            # Temporarily add back previously satisfied relationships
21            rest += (l[le[i]] <= l[i]) + (l[i] <= l[r]) + (l[r] <= l[rr])
22            
23            # Merge the pair
24            le[rr], ri[i] = i, rr
25            l[i] = v
26            
27            # Subtract satisfied relationships with new value
28            rest -= 1 + (l[le[i]] <= l[i]) + (l[i] <= l[rr])
29
30            # Push updated adjacent pairs into heap
31            if i:
32                heappush(h, (l[le[i]] + l[i], le[i]))
33            if rr < n:
34                heappush(h, (l[i] + l[rr], i))
35
36            ans += 1
37        
38        return ans