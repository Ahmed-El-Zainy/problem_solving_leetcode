1class Solution:
2    def minimumCost(self, nums: List[int]) -> int:
3        if len(nums) == 3:
4            return sum(nums)
5
6        # nums[0] is always included
7        rest = nums[1:]
8        rest.sort()
9
10        return nums[0] + rest[0] + rest[1]