1class Solution:
2    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
3        arr.sort()
4        diff = arr[1] - arr[0]
5        for i in range(1, len(arr)):
6            if arr[i] - arr[i-1] != diff:
7                return False
8        return True