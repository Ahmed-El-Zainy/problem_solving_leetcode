1import heapq
2from typing import List
3class Solution:
4    def minCost(self, grid: List[List[int]], k: int) -> int:
5        m, n = len(grid), len(grid[0])
6        INF = 10**18
7        
8        # dist[i][j][t] = min cost to reach (i,j) using t teleports
9        dist = [[[INF] * (k + 1) for _ in range(n)] for _ in range(m)]
10        dist[0][0][0] = 0
11        
12        # cells sorted by value for teleport handling
13        cells = sorted((grid[i][j], i, j) for i in range(m) for j in range(n))
14        
15        pq = [(0, 0, 0, 0)]  # cost, i, j, teleports_used
16        
17        # teleport pointers per teleport count
18        used = [0] * (k + 1)
19        
20        while pq:
21            cost, i, j, t = heapq.heappop(pq)
22            if cost > dist[i][j][t]:
23                continue
24            
25            # reached destination
26            if i == m - 1 and j == n - 1:
27                return cost
28            
29            # normal moves
30            for ni, nj in ((i + 1, j), (i, j + 1)):
31                if ni < m and nj < n:
32                    nc = cost + grid[ni][nj]
33                    if nc < dist[ni][nj][t]:
34                        dist[ni][nj][t] = nc
35                        heapq.heappush(pq, (nc, ni, nj, t))
36            
37            # teleport
38            if t < k:
39                while used[t] < len(cells) and cells[used[t]][0] <= grid[i][j]:
40                    _, x, y = cells[used[t]]
41                    if cost < dist[x][y][t + 1]:
42                        dist[x][y][t + 1] = cost
43                        heapq.heappush(pq, (cost, x, y, t + 1))
44                    used[t] += 1
45        
46        return -1