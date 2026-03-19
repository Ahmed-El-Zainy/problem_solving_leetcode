#
# @lc app=leetcode id=3070 lang=python3
#
# [3070] Count Submatrices with Top-Left Element and Sum Less Than k
#
# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/description/
#
# algorithms
# Medium (58.25%)
# Likes:    324
# Dislikes: 13
# Total Accepted:    67.8K
# Total Submissions: 97.7K
# Testcase Example:  '[[7,6,3],[6,6,1]]\n18'
#
# You are given a 0-indexed integer matrix grid and an integer k.
# 
# Return the number of submatrices that contain the top-left element of the
# grid, and have a sum less than or equal to k.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[7,6,3],[6,6,1]], k = 18
# Output: 4
# Explanation: There are only 4 submatrices, shown in the image above, that
# contain the top-left element of grid, and have a sum less than or equal to
# 18.
# 
# Example 2:
# 
# 
# Input: grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20
# Output: 6
# Explanation: There are only 6 submatrices, shown in the image above, that
# contain the top-left element of grid, and have a sum less than or equal to
# 20.
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length 
# n == grid[i].length
# 1 <= n, m <= 1000 
# 0 <= grid[i][j] <= 1000
# 1 <= k <= 10^9
# 
# 
#
from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        """
        Count submatrices that contain the top-left element (0,0) with sum <= k.
        
        Key insight: Any submatrix containing grid[0][0] must have its top-left 
        corner at (0,0). So we only need to consider submatrices defined by 
        their bottom-right corner (i,j), and check if sum from (0,0) to (i,j) <= k.
        
        We use 2D prefix sums to efficiently calculate these cumulative sums.
        """
        m, n = len(grid), len(grid[0])
        
        # prefix[i+1][j+1] represents sum of submatrix from (0,0) to (i,j)
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        count = 0
        for i in range(m):
            for j in range(n):
                # 2D prefix sum formula:
                # current = grid[i][j] + top + left - topleft (to avoid double counting)
                prefix[i+1][j+1] = (grid[i][j] + prefix[i][j+1] + 
                                   prefix[i+1][j] - prefix[i][j])
                
                # Check if submatrix (0,0) to (i,j) has sum <= k
                if prefix[i+1][j+1] <= k:
                    count += 1
        
        return count# @lc code=end

