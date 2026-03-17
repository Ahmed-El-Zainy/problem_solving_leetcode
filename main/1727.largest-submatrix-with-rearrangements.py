#
# @lc app=leetcode id=1727 lang=python3
#
# [1727] Largest Submatrix With Rearrangements
#
# https://leetcode.com/problems/largest-submatrix-with-rearrangements/description/
#
# algorithms
# Medium (75.22%)
# Likes:    2248
# Dislikes: 128
# Total Accepted:    147.1K
# Total Submissions: 183.4K
# Testcase Example:  '[[0,0,1],[1,1,1],[1,0,1]]'
#
# You are given a binary matrix matrix of size m x n, and you are allowed to
# rearrange the columns of the matrix in any order.
# 
# Return the area of the largest submatrix within matrix where every element of
# the submatrix is 1 after reordering the columns optimally.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
# Output: 4
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 4.
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,0,1,0,1]]
# Output: 3
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 3.
# 
# 
# Example 3:
# 
# 
# Input: matrix = [[1,1,0],[1,0,1]]
# Output: 2
# Explanation: Notice that you must rearrange entire columns, and there is no
# way to make a submatrix of 1s larger than an area of 2.
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m * n <= 10^5
# matrix[i][j] is either 0 or 1.
# 
# 
#

# @lc code=start

from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        """
        Find the largest submatrix of 1s after optimally rearranging columns.
        
        Key insight: Since we can rearrange columns arbitrarily, for each row,
        we can treat the heights of consecutive 1s as a histogram and sort them
        to find the maximum rectangle area.
        
        Algorithm:
        1. Compute height of consecutive 1s for each cell (going upward)
        2. For each row, sort heights in descending order
        3. For each position j in sorted row: area = height[j] * (j+1)
           (we can pick j+1 columns with height >= height[j])
        4. Track maximum area across all rows
        """
        m, n = len(matrix), len(matrix[0])
        
        # Step 1: Calculate height of consecutive 1s ending at each cell
        # If matrix[i][j] == 1, accumulate height from row above
        # If matrix[i][j] == 0, height resets to 0
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
        
        max_area = 0
        
        # Step 2-4: For each row, sort heights and calculate max rectangle area
        for i in range(m):
            # Sort current row's heights in descending order
            # This simulates optimal column rearrangement
            matrix[i].sort(reverse=True)
            
            # Calculate max area for this row as base
            for j in range(n):
                # Width = j+1 (number of columns we can use)
                # Height = matrix[i][j] (minimum height among these columns)
                area = matrix[i][j] * (j + 1)
                max_area = max(max_area, area)
        
        return max_area
# @lc code=end

