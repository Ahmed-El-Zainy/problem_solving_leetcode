1class Solution:
2    def minimumDifference(self, nums: List[int], k: int) -> int:
3        nums.sort()
4        min_diff = float('inf')
5        for i in range(len(nums) - k + 1):
6            diff = nums[i + k - 1] - nums[i]
7            min_diff = min(min_diff, diff)
8        return min_diff