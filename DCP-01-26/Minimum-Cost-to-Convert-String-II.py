1INF = 10**18
2INF_INT = 10**9
3
4
5class Solution:
6    def minimumCost(
7        self,
8        source: str,
9        target: str,
10        original: List[str],
11        changed: List[str],
12        cost: List[int],
13    ) -> int:
14        n = len(source)
15        m = len(original)
16
17        child = [[-1] * 26]
18        tid = [-1]
19
20        def new_node() -> int:
21            child.append([-1] * 26)
22            tid.append(-1)
23            return len(child) - 1
24
25        idx = -1
26
27        def add(word: str) -> int:
28            nonlocal idx
29            node = 0
30            for ch in word:
31                c = ord(ch) - 97
32                nxt = child[node][c]
33                if nxt == -1:
34                    nxt = new_node()
35                    child[node][c] = nxt
36                node = nxt
37            if tid[node] == -1:
38                idx += 1
39                tid[node] = idx
40            return tid[node]
41
42        edges = []
43        for i in range(m):
44            x = add(original[i])
45            y = add(changed[i])
46            edges.append((x, y, cost[i]))
47
48        P = idx + 1
49        if P == 0:
50            return 0 if source == target else -1
51
52        dist = [[INF_INT] * P for _ in range(P)]
53        for i in range(P):
54            dist[i][i] = 0
55        for x, y, w in edges:
56            if w < dist[x][y]:
57                dist[x][y] = w
58
59        for k in range(P):
60            dk = dist[k]
61            for i in range(P):
62                di = dist[i]
63                dik = di[k]
64                if dik == INF_INT:
65                    continue
66                base = dik
67                for j in range(P):
68                    nd = base + dk[j]
69                    if nd < di[j]:
70                        di[j] = nd
71
72        dp = [INF] * (n + 1)
73        dp[0] = 0
74
75        s_arr = [ord(c) - 97 for c in source]
76        t_arr = [ord(c) - 97 for c in target]
77
78        for j in range(n):
79            if dp[j] >= INF:
80                continue
81
82            base = dp[j]
83
84            if source[j] == target[j] and base < dp[j + 1]:
85                dp[j + 1] = base
86
87            u = 0
88            v = 0
89            for i in range(j, n):
90                u = child[u][s_arr[i]]
91                v = child[v][t_arr[i]]
92                if u == -1 or v == -1:
93                    break
94                uid = tid[u]
95                vid = tid[v]
96                if uid != -1 and vid != -1:
97                    w = dist[uid][vid]
98                    if w != INF_INT:
99                        ni = i + 1
100                        cand = base + w
101                        if cand < dp[ni]:
102                            dp[ni] = cand
103
104        ans = dp[n]
105        return -1 if ans >= INF else ans