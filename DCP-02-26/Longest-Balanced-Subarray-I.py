1class Solution:
2    def longestBalanced(self, nums: List[int]) -> int:
3        ans = 0
4        for i in range(len(nums)):
5            even , odd = set(), set()
6            for j in range(i, len(nums)):
7                if nums[j] % 2 ==0 :
8                    even.add(nums[j])
9                else:
10                    odd.add(nums[j])
11                if len(odd) == len(even):
12                    ans = max(ans, j - i + 1)
13        return ans