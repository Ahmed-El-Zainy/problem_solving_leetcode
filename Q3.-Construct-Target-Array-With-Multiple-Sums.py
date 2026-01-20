1import heapq
2class Solution:
3    def isPossible(self, target: List[int]) -> bool:
4        total = sum(target)
5        heap = [-x for x in target]
6        heapq.heapify(heap)
7        while True:
8            largest = -heapq.heappop(heap)
9            rest = total - largest
10            if largest==1 or rest==1:
11                return True
12            if rest==0 or rest >= largest:
13                return False
14                
15            prev = largest % rest
16            if prev ==0 :
17                return False
18            heapq.heappush(heap, -prev)
19            total = prev + rest