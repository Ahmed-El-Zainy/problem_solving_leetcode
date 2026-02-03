1
2from typing import List
3# @lc code=start
4class Solution:
5    def isTrionic(self, nums: List[int]) -> bool:
6        n = len(nums)
7        if n < 3:
8            return False
9
10        i = 0
11
12        # Ascending phase
13        while i + 1 < n and nums[i] < nums[i + 1]:
14            i += 1
15
16        # Check if we have at least one element in the ascending phase
17        if i == 0:
18            return False
19
20        # Descending phase
21        j = i
22        while j + 1 < n and nums[j] > nums[j + 1]:
23            j += 1
24
25        # Check if we have at least one element in the descending phase
26        if j == i:
27            return False
28
29        # Final ascending phase
30        k = j
31        while k + 1 < n and nums[k] < nums[k + 1]:
32            k += 1
33
34        # Check if we have at least one element in the final ascending phase
35        if k == j:
36            return False
37
38        # If we reached the end of the array, it's trionic
39        return k == n - 1
40        
41