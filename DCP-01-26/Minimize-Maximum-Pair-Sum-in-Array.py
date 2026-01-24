1class Solution:
2    def minPairSum(self, nums: List[int]) -> int:
3        sorted_nums = sorted(nums)
4        max_pair_sum = 0
5        for i in range(len(sorted_nums)//2):
6            max_pair_sum = max(max_pair_sum, sorted_nums[i] + sorted_nums[-i-1])
7        return max_pair_sum