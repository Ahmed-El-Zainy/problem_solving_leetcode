1class Solution:
2    def lastStoneWeight(self, stones: List[int]) -> int:
3        stones = [-s for s in stones]
4        heapq.heapify(stones)
5        while len(stones) > 1:
6            y = - heapq.heappop(stones)
7            x = - heapq.heappop(stones)
8            if y != x:
9                heapq.heappush(stones, -(y - x))
10        return -stones[0] if stones else 0