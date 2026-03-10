1class Solution:
2    def minOperations(self, s: str, k: int) -> int:
3        n = len(s)
4        z = s.count('0')
5        o = n - z
6        
7        if z == 0:
8            return 0
9        
10        for ops in range(1, 2 * n + 2):
11            total = ops * k
12            if total < z:
13                continue
14            extra = total - z
15            if extra % 2 != 0:
16                continue
17            # Each of the z zeros gets odd flips (min 1, max ops)
18            # Each of the o ones gets even flips (min 0, max ops)
19            # Max extra we can absorb:
20            # - each zero can take up to (ops-1) extra (must stay odd), so floor((ops-1)/2)*2 extra per zero
21            # - each one can take up to ops extra (must stay even), so floor(ops/2)*2 extra per one
22            max_extra = z * ((ops - 1) // 2 * 2) + o * (ops // 2 * 2)
23            if extra <= max_extra:
24                return ops
25        
26        return -1