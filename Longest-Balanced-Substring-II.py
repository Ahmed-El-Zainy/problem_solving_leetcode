1class Solution:
2    def longestBalanced(self, s: str) -> int:
3        n=len(s)
4        # Deal with 1-letter balance
5        ans, Len=1, 1
6        for c0, c1 in pairwise(s):
7            if c0==c1: Len+=1
8            else:
9                ans=max(ans, Len)
10                Len=1
11        ans=max(ans, Len)
12
13        ab, bc, ca, abc={},{},{},{}
14        abc[(0, 0)]=ab[(0, 0)]=bc[(0, 0)]=ca[(0, 0)]=-1
15
16        cnt=[0, 0, 0]
17        for i, c in enumerate(s):
18            cnt[ord(c)-97]+=1
19            A, B, C=cnt
20
21            # 3-letter balance: A=B=C
22            key=(B-A, C-A)
23            if  key in abc: ans=max(ans, i-abc[key])
24            else: abc[key]=i
25
26            # 2-letter balance:
27            key=(A-B, C)
28            if  key in ab: ans=max(ans, i-ab[key])
29            else: ab[key]=i
30
31            key=(B-C, A)
32            if  key in bc: ans=max(ans, i-bc[key])
33            else: bc[key]=i
34
35            key=(C-A, B)
36            if  key in ca: ans=max(ans, i-ca[key])
37            else: ca[key]=i
38        return ans    