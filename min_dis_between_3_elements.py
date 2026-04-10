
"""
3740. Minimum Distance Between Three Equal Elements I
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].

The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.

Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.

 

Example 1:

Input: nums = [1,2,1,1,3]

Output: 6

Explanation:

The minimum distance is achieved by the good tuple (0, 2, 3).

(0, 2, 3) is a good tuple because nums[0] == nums[2] == nums[3] == 1. Its distance is abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6.

Example 2:
    
Input: nums = [1,1,2,3,2,1,2]

Output: 8

Explanation:

The minimum distance is achieved by the good tuple (2, 4, 6).

(2, 4, 6) is a good tuple because nums[2] == nums[4] == nums[6] == 2. Its distance is abs(2 - 4) + abs(4 - 6) + abs(6 - 2) = 2 + 2 + 4 = 8.

Example 3:

Input: nums = [1]

Output: -1

Explanation:

There are no good tuples. Therefore, the answer is -1.

"""

from collections import defaultdict
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        index_map = defaultdict(list)
        
        # Step 1: group indices
        for i, num in enumerate(nums):
            index_map[num].append(i)
        
        ans = float('inf')
        
        # Step 2: process each value
        for indices in index_map.values():
            if len(indices) < 3:
                continue
            
            # Step 3: check consecutive triples
            for i in range(len(indices) - 2):
                left = indices[i]
                right = indices[i + 2]
                ans = min(ans, 2 * (right - left))
        
        return ans if ans != float('inf') else -1
if __name__=="__main__":

    nums = [1]
    output = -1
    sol = Solution()
    print(f"output:{output}, code_output: {sol.minimumDistance(nums)}")



