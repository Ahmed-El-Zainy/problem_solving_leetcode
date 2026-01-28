1class Solution:
2    def minCost(self, grid: List[List[int]], k: int) -> int:
3        n = len(grid[0])
4        mx = max(map(max, grid))
5        suf_min_f = [inf] * (mx + 2)
6        for _ in range(k + 1):
7            min_f = [inf] * (mx + 1)
8            f = [inf] * (n + 1)
9            f[1] = -grid[0][0]
10            for row in grid:
11                for j, x in enumerate(row):
12                    v = f[j+1]
13                    if f[j] < v: v = f[j]
14                    v += x
15                    if suf_min_f[x] < v: v = suf_min_f[x]
16                    f[j + 1] = v
17                    if f[j + 1] < min_f[x]: min_f[x] = f[j + 1]
18            tmp = suf_min_f.copy()
19            for i in range(mx, -1, -1):
20                v = suf_min_f[i + 1]
21                if min_f[i] < v: v = min_f[i]
22                suf_min_f[i] = v
23            if suf_min_f == tmp:
24                break
25        return f[n]
26
27
28
29
30