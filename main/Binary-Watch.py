1class Solution:
2    def readBinaryWatch(self, turnedOn: int) -> List[str]:
3        
4        def countBits(x: int) -> int:
5            count = 0
6            while x:
7                count += 1
8                x &= x - 1
9            return count
10
11        times = []
12        for h in range(12):
13            for m in range(60):
14                if countBits(h) + countBits(m) == turnedOn:
15                    times.append(f"{h}:{m:02d}")
16        return times