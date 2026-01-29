1class Solution:
2    def minimumCost(
3        self,
4        source: str,
5        target: str,
6        original: list[str],
7        changed: list[str],
8        cost: list[int]
9    ) -> int:
10        
11        INF = 10**18
12        N = 26
13        
14        # dist[a][b] = min cost to convert char a -> b
15        dist = [[INF] * N for _ in range(N)]
16        
17        for i in range(N):
18            dist[i][i] = 0
19        
20        # initialize edges
21        for o, c, w in zip(original, changed, cost):
22            u = ord(o) - ord('a')
23            v = ord(c) - ord('a')
24            dist[u][v] = min(dist[u][v], w)
25        
26        # Floyd–Warshall
27        for k in range(N):
28            for i in range(N):
29                for j in range(N):
30                    if dist[i][k] + dist[k][j] < dist[i][j]:
31                        dist[i][j] = dist[i][k] + dist[k][j]
32        
33        # compute answer
34        ans = 0
35        for s, t in zip(source, target):
36            if s == t:
37                continue
38            u = ord(s) - ord('a')
39            v = ord(t) - ord('a')
40            if dist[u][v] == INF:
41                return -1
42            ans += dist[u][v]
43        
44        return ans