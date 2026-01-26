1class Solution:
2    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
3        arr.sort()
4        min_diff = float('inf')
5        result = []
6        # First pass: find minimum difference
7        for i in range(len(arr) - 1):
8            min_diff = min(min_diff, arr[i + 1] - arr[i])
9
10        # Second pass: collect all pairs with min difference
11        for i in range(len(arr) - 1):
12            if arr[i + 1] - arr[i] == min_diff:
13                result.append([arr[i], arr[i + 1]])
14
15        return result