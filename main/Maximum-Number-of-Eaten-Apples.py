1class Solution:
2    def eatenApples(self, apples: List[int], days: List[int]) -> int:
3        heap = []
4        eaten = 0
5        day = 0
6        n = len(apples)
7
8        while day < n or heap:
9            # Add new apples of the day
10            if day < n and apples[day] > 0:
11                expiry = day + days[day]
12                heapq.heappush(heap, (expiry, apples[day]))
13
14            # Remove rotten apples
15            while heap and heap[0][0] <= day:
16                heapq.heappop(heap)
17
18            # Eat one apple
19            if heap:
20                expiry, count = heapq.heappop(heap)
21                eaten += 1
22                if count > 1:
23                    heapq.heappush(heap, (expiry, count - 1))
24            day += 1
25
26        return eaten