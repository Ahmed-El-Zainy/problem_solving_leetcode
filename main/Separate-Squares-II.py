1class Solution:
2    def separateSquares(self, squares: List[List[int]]) -> float:
3        events = []
4        for x, y, l in squares:
5            events.append((y, 1, x, x + l))
6            events.append((y + l, -1, x, x + l))
7
8        events.sort()
9        xs = []
10        prev_y = events[0][0]
11        total = 0
12        areas = []
13
14        def union_len(intervals):
15            intervals.sort()
16            res = cur = 0
17            end = -10**30
18            for a, b in intervals:
19                if a > end:
20                    res += b - a
21                    end = b
22                elif b > end:
23                    res += b - end
24                    end = b
25            return res
26
27        for y, typ, x1, x2 in events:
28            if y > prev_y and xs:
29                h = y - prev_y
30                w = union_len(xs)
31                areas.append((prev_y, h, w))
32                total += h * w
33            if typ == 1:
34                xs.append((x1, x2))
35            else:
36                xs.remove((x1, x2))
37            prev_y = y
38
39        half = total / 2
40        acc = 0
41        for y, h, w in areas:
42            if acc + h * w >= half:
43                return y + (half - acc) / w
44            acc += h * w
45
46        return 0.0