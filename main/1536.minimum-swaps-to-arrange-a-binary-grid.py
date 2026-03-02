#
# @lc app=leetcode id=1536 lang=python3
#
# [1536] Minimum Swaps to Arrange a Binary Grid
#
# https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/description/
#
# algorithms
# Medium (49.18%)
# Likes:    600
# Dislikes: 75
# Total Accepted:    21.1K
# Total Submissions: 41K
# Testcase Example:  '[[0,0,1],[1,1,0],[1,0,0]]'
#
# Given an n x n binary grid, in one step you can choose two adjacent rows of
# the grid and swap them.
# 
# A grid is said to be valid if all the cells above the main diagonal are
# zeros.
# 
# Return the minimum number of steps needed to make the grid valid, or -1 if
# the grid cannot be valid.
# 
# The main diagonal of a grid is the diagonal that starts at cell (1, 1) and
# ends at cell (n, n).
# 
# 
# Example 1:
# 
# 
# Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# Output: -1
# Explanation: All rows are similar, swaps have no effect on the grid.
# 
# 
# Example 3:
# 
# 
# Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# n == grid.length == grid[i].length
# 1 <= n <= 200
# grid[i][j] is either 0 or 1
# 
# 
#

# @lc code=start
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        # Count the number of trailing zeros in each row
        trailing_zeros = []
        for row in grid:
            count = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)

        swaps = 0
        for i in range(n):
            required_zeros = n - 1 - i
            found = False
            for j in range(i, n):
                if trailing_zeros[j] >= required_zeros:
                    found = True
                    # Swap the rows in the trailing_zeros list
                    while j > i:
                        trailing_zeros[j], trailing_zeros[j - 1] = trailing_zeros[j - 1], trailing_zeros[j]
                        j -= 1
                        swaps += 1
                    break
            
            if not found:
                return -1
        
        return swaps

# @lc code=end

