1class Solution:
2    def minimumPairRemoval(self, nums: List[int]) -> int:
3        count = 0
4
5        while len(nums) > 1:
6            isAscending = True
7            minSum = float("inf")
8            targetIndex = -1
9
10            for i in range(len(nums) - 1):
11                pair_sum = nums[i] + nums[i + 1]
12
13                if nums[i] > nums[i + 1]:
14                    isAscending = False
15
16                if pair_sum < minSum:
17                    minSum = pair_sum
18                    targetIndex = i
19
20            if isAscending:
21                break
22
23            count += 1
24            nums[targetIndex] = minSum
25            nums.pop(targetIndex + 1)
26
27        return count