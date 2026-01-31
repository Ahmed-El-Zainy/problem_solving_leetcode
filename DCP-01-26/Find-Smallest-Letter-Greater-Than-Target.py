1class Solution:
2    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
3        n = len(letters)
4        low = 0; high = n-1
5        min1 = "z" 
6        count = 0
7        while low<=high:
8            mid = (low+high)//2
9            if letters[mid] > target:
10                min1 = min(letters[mid],min1)
11                high = mid - 1
12                count = 1
13            else:
14                low = mid + 1
15        if count == 0:
16            return letters[0]
17        else:
18            return min1
19        