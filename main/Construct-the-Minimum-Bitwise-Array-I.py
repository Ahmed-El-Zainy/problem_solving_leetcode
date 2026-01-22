1class Solution:
2    def minBitwiseArray(self, nums: List[int]) -> List[int]:
3        ans = []
4        for x in nums:
5            if x == 2:
6                ans.append(-1)
7            else:
8                bit = (x + 1) & -(x + 1)
9                ans.append(x - (bit >> 1))
10        return ans