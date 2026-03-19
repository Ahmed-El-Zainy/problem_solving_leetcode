#
# @lc app=leetcode id=3212 lang=python3
#
# [3212] Count Submatrices With Equal Frequency of X and Y
#
# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/description/
#
# algorithms
# Medium (51.46%)
# Likes:    390
# Dislikes: 49
# Total Accepted:    96.7K
# Total Submissions: 140.1K
# Testcase Example:  '[["X","Y","."],["Y",".","."]]'
#
# Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or
# '.', return the number of submatrices that contain:
# 
# 
# grid[0][0]
# an equal frequency of 'X' and 'Y'.
# at least one 'X'.
# 
# 
# 
# Example 1:
# 
# 
# Input: grid = [["X","Y","."],["Y",".","."]]
# 
# Output: 3
# 
# Explanation:
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: grid = [["X","X"],["X","Y"]]
# 
# Output: 0
# 
# Explanation:
# 
# No submatrix has an equal frequency of 'X' and 'Y'.
# 
# 
# Example 3:
# 
# 
# Input: grid = [[".","."],[".","."]]
# 
# Output: 0
# 
# Explanation:
# 
# No submatrix has at least one 'X'.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= grid.length, grid[i].length <= 1000
# grid[i][j] is either 'X', 'Y', or '.'.
# 
# 
#
from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        """
        Count submatrices containing grid[0][0] with equal frequency of 'X' and 'Y',
        and at least one 'X'.
        
        Key insight: Since submatrix must contain grid[0][0], its top-left corner
        is fixed at (0,0). We only need to check submatrices defined by their
        bottom-right corner (i,j).
        
        Use 2D prefix sums to track counts of 'X' and 'Y' separately for O(1) queries.
        """
        m, n = len(grid), len(grid[0])
        
        # prefix_x[i+1][j+1] = count of 'X' in submatrix from (0,0) to (i,j)
        # prefix_y[i+1][j+1] = count of 'Y' in submatrix from (0,0) to (i,j)
        prefix_x = [[0] * (n + 1) for _ in range(m + 1)]
        prefix_y = [[0] * (n + 1) for _ in range(m + 1)]
        
        count = 0
        for i in range(m):
            for j in range(n):
                # Convert current cell to counts
                is_x = 1 if grid[i][j] == 'X' else 0
                is_y = 1 if grid[i][j] == 'Y' else 0
                
                # 2D prefix sum formula (inclusion-exclusion principle)
                prefix_x[i+1][j+1] = (is_x + prefix_x[i][j+1] + 
                                     prefix_x[i+1][j] - prefix_x[i][j])
                prefix_y[i+1][j+1] = (is_y + prefix_y[i][j+1] + 
                                     prefix_y[i+1][j] - prefix_y[i][j])
                
                # Check both conditions:
                # 1. Equal frequency of X and Y
                # 2. At least one X (implies at least one Y too, since they're equal)
                if prefix_x[i+1][j+1] == prefix_y[i+1][j+1] and prefix_x[i+1][j+1] >= 1:
                    count += 1
        
        return count


# @lc code=end

