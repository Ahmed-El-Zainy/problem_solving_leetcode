1from collections import defaultdict
2import heapq
3class Solution:
4    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
5        # build adjacency list
6        adj_list = defaultdict(list)
7        for idx in range(len(original)):
8            adj_list[original[idx]].append((cost[idx], changed[idx]))
9        
10        # do n^2 dfs to find shortest path length
11        dfs = defaultdict(lambda: defaultdict(lambda: float('inf')))
12        for start in original:
13            # disjktra with this start node
14            dfs[start][start] = 0
15            pq = [(0, start)]
16            visited = set()
17            while pq:
18                dist, vtx = heapq.heappop(pq)
19                if vtx in visited:
20                    continue
21                visited.add(vtx)
22                dfs[start][vtx] = dist
23                # then add to queue
24                for cost, child in adj_list[vtx]:
25                    new_dist = dist + cost
26                    if child not in visited:
27                        heapq.heappush(pq, (new_dist, child))
28        
29        ## this below part is what takes too long ##
30        n = len(source)
31        INF = float('inf')
32        dp = [INF] * (n + 1)
33        dp[0] = 0
34
35        original_set = set(original)
36        changed_set = set(changed)
37        valid_lengths = set(len(s) for s in original_set)
38
39        for i in range(n):
40            if dp[i] == INF:
41                continue
42
43            # Case 1: no-op if characters match
44            if source[i] == target[i]:
45                dp[i + 1] = min(dp[i + 1], dp[i])
46
47            # Case 2: try transformations
48            for L in valid_lengths:
49                if i + L > n:
50                    continue
51
52                s_sub = source[i:i + L]
53                if s_sub not in original_set:
54                    continue
55
56                t_sub = target[i:i + L]
57                cost_val = dfs[s_sub][t_sub]
58                if cost_val < INF:
59                    dp[i + L] = min(dp[i + L], dp[i] + cost_val)
60        return -1 if dp[n] == INF else dp[n]