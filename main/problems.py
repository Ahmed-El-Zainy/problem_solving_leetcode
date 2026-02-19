import collections
from collections import Counter
import numpy as np
from itertools import combinations
import heapq
from typing import Optional, List
from collections import deque

# problem solving


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Input: nums = [1,1,2]
        # Output: 2, nums = [1,2,_]
        # c_nums = sorted(nums)
        # result = []
        # for i in range(len(c_nums)):
        #     if c_nums[i] not in result:
        #         result.append(c_nums[i])
        #     else:
        #         result.append("_")
        # return result
        c_nums = sorted(nums)
        result = []
        duplicates = set()
        for num in c_nums:
            if num not in duplicates:
                result.append(num)
                duplicates.add(num)
            else:
                result.append('_')
            # Split result into numbers and "_" parts
        numbers = [num for num in result if num != '_']
        return numbers

    def check_duplicate_improved(self, nums):
            nums.sort()
            index = 0
            for i in range(len(nums) - 1):  # Subtract 1 from the range
                if nums[i] != nums[i + 1]:  # Compare current element with the next one
                    nums[index] = nums[i]
                    index += 1
            nums[index] = nums[-1]
            return index + 1  # Return the index incremented by 1


    def remove_element(self, nums, val):
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i] = nums[index]
                index += 1
        return index

    def pop(self, nums, val):
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index

    def next_Permutation(self, numbers):
        i = len(numbers) - 2
        while i >= 0 and numbers[i] >= numbers[i + 1]:
            i -= 1

        if i >= 0:
            # Find the smallest element from the right which is greater than arr[i]
            j = len(numbers) - 1
            while numbers[j] <= numbers[i]:
                j -= 1

            # Swap arr[i] and arr[j]
            numbers[i], numbers[j] = numbers[j], numbers[i]

        # Reverse the elements after index i to get the next permutation
        left, right = i + 1, len(numbers) - 1
        while left < right:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left += 1
            right -= 1
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        sum_values = []
        for _ in range(k):
            max_value = max(happiness)
            sum_values += max_value

            max_index = happiness.index(max_value)
            happiness[max_index] = max(0, happiness[max_index -1])
            happiness = [max(0, num -1) for num in happiness]

        return sum_values
# class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        heap = [(-arr[i] / arr[-1], i, len(arr) - 1) for i in range(len(arr) - 1)]
        heapq.heapify(heap)
        for _ in range(k):
            fraction, numerator_index, dominrator_index = heapq.heappop(heap)
            if dominrator_index - 1 > numerator_index:
                next_fraction = -arr[numerator_index] / arr[dominrator_index -1]
                heapq.heappush(heap, (next_fraction, numerator_index, dominrator_index -1))
        fraction, numerator_index, dominrator_index = heapq.heappop(heap)
        return [arr[numerator_index], arr[dominrator_index]]


    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        workers = sorted((w / q, q, w) for w, q in zip(wage, quality))
        heap = []
        sum_quality = 0
        min_cost = float('inf')
        for ratio, q, w in workers:
            heapq.heappush(heap, -q)
            sum_quality += q

            if len(heap) > k:
                sum_quality += heapq.heappop(heap)

            if len(heap) == k:
                min_cost = min(min_cost, ratio * sum_quality)
        return float(min_cost)

    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        max_local = [[0]* (n-2) for _ in range(n-2)]
        for i in range(1, n-1):
            for j in range(1, n-1):
                sub_matrix = [grid[x][y] for x in range(i - 1, i + 2) for y in range(j - 1, j + 2)]
                max_local[i-1][j-1] = max(sub_matrix)
        return max_local

    def matrixScore(self, grid: list[list[int]]) -> int:
        # if raw start with 0 -> then flip it
        # if the number of the os in the column bigger than 1s flip it
        for row in grid:
            if row[0] == 0:
                row[:] = [1- cell for cell in row]

        for j in range(len(grid[1])):
            count_0 = sum(row[j] == 0 for row in grid)
            count_1 = sum(row[j] == 1 for row in grid)
            if count_0 > count_1:
                for column in grid:
                    column[j] = 1 - column[j]
            # Convert each row to decimal and sum them
        total = 0
        for row in grid:
            binary_str = ''.join(str(cell) for cell in row)
            decimal = int(binary_str, 2)
            total += decimal
        return total

    def threeSum(self, nums: list[int]) -> list[list[int]]:
            nums.sort()
            result = []
            for i in range(len(nums) - 2):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                start, end = i + 1, len(nums) - 1
                while start < end:
                    total = nums[i] + nums[start] + nums[end]
                    if total == 0:
                        result.append([nums[i], nums[start], nums[end]])
                        while start < end and nums[start] == nums[start + 1]:
                            start += 1
                        while start < end and nums[end] == nums[end - 1]:
                            end -= 1
                        start += 1
                        end -= 1
                    elif total < 0:
                        start += 1
                    else:
                        end -= 1
            return result

    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == target:
                    return current_sum
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        return closest_sum
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        reversed_str = str(abs(x))[::-1]
        reversed_sum = sign * int(reversed_str)
        return reversed_sum

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        result = sorted(nums1 + nums2)
        n = len(result)
        mid = n // 2
        if n % 2 == 0:
            median = (result[mid - 1] + result[mid]) / 2
        else:
            median = result[mid]
        return float(median)

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        res = [root]
        for i in range(len(root)):
            if (res[i] == target) & (res[0] != target):
                res.remove(res[i])
        return res

    # Definition for a binary tree node.



    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def dfs(node):
            if not node:
                return 0
            print(f"node; {node}")
            left = dfs(node.left)
            print(f"left: {left}")
            right = dfs(node.right)
            pritn(f"right: {right}")
            self.moves += abs(left) + abs(right)
            print(f"moves: {self.moves}")
            return node.val + left + right - 1

        dfs(root)
        return self.moves

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        for i in range(1 << n):
            subset = []
            for j in range(n):
                if i & (1 << j):
                    print(f'nums[j]: {nums[j]}')
                    subset.append(nums[j])
            print(f'subset: {subset}')
            result.append(subset)
        return result

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # differences = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        # return differences
        curCost = 0
        l = 0
        res = 0
        for r in range(len(s)):
            curCost += abs(ord(s[r]) - ord(t[r]))

            while curCost > maxCost:
                curCost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            res = max(res, r - l + 1)
        return res
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # Sliding Window with Array
        total = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                total += customers[i]
                customers[i] = 0

        max_grumpy = sum(customers[:minutes])
        print(f'total: {total}')
        print(f'max_grumpy before : {max_grumpy}')
        window_sum = max_grumpy

        for i in range(minutes, len(customers)):
            window_sum = window_sum + customers[i] - customers[i - minutes]
            max_grumpy = max(max_grumpy, window_sum)
            print(f'window_sum: {window_sum}')
            print(f'max_grumpy: {max_grumpy}')
        return total + max_grumpy

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = collections.defaultdict(int)
        count[0] = 1
        previous_num = res = 0
        for num in nums:
            previous_num += num % 2
            if previous_num >= k:
                res += count[previous_num - k]
            count[previous_num] += 1
        return res

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        que = deque()
        res = 0
        for i in range(n):
            if que and i >= que[0] + k:
                que.popleft()
            if len(que) % 2 == nums[i]:
                if i + k > n:
                    return -1
                que.append(i)
                res += 1
        return res
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.total = 0 
        def dfs(node):
            if node:
                dfs(node.right)
                self.total+= node.val
                node.val = self.total
                dfs(node.left)
        dfs(root)
        return root





if __name__ == "__main__":
    # nums = [1, 2, 3, 4, 5]
    # quality = [10, 20, 5]
    # wage = [70, 50, 30]
    # k = 2
    # quality, wage, k = [3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3
    # print(Solution.next_Permutation(Solution, nums))
    # res = Solution.mincostToHireWorkers(Solution, quality, wage, k)
    # print(res)
    # grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    # grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
    # grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
    # nums = [-1, 0, 1, 2, -1, -4]
    # Output: [[-1, -1, 2], [-1, 0, 1]]
    # x = 120
    # input = 1534236469
    # Output: 9646324351
    # pred  : 9646324351
    # nums1, nums2 = [1, 2], [3, 4]
    # root = [0, 3, 0]
    # Output: [1, null, 3, null, 4]
    # nums = [1, 2, 3]
    # Output = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    # print('Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]')
    # print(f'predicted: {Solution.subsets(Solution, nums)}')
    # s = "abcd"
    # t = "cdef"
    # maxCost = 3
    # customers = [1, 0, 1, 2, 1, 1, 7, 5]
    # grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    # minutes = 3
    # nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
    # k = 2

    # nums = [0, 1, 0]
    # k = 1
    
    root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
    print(Solution.bstToGst(Solution, root=root))
    # print(f"differences: {Solution.equalSubstring(Solution, s, t, maxCost)}")




