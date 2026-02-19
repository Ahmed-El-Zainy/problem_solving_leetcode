1import heapq
2from typing import List
3
4class Solution:
5    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
6        if not nums1 or not nums2:
7            return []
8        
9        heap = []
10        result = []
11
12        # initialize heap
13        for i in range(min(k, len(nums1))):
14            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
15
16        while heap and k > 0:
17            _, i, j = heapq.heappop(heap)
18            result.append([nums1[i], nums2[j]])
19            k -= 1
20
21            if j + 1 < len(nums2):
22                heapq.heappush(
23                    heap,
24                    (nums1[i] + nums2[j + 1], i, j + 1)
25                )
26
27        return result
28