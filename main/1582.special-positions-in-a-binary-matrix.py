#
# @lc app=leetcode id=1582 lang=python3
#
# [1582] Special Positions in a Binary Matrix
#
# https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/
#
# algorithms
# Easy (68.82%)
# Likes:    1746
# Dislikes: 80
# Total Accepted:    252.3K
# Total Submissions: 350.4K
# Testcase Example:  '[[1,0,0],[0,0,1],[1,0,0]]'
#
# Given an m x n binary matrix mat, return the number of special positions in
# mat.
# 
# A position (i, j) is called special if mat[i][j] == 1 and all other elements
# in row i and column j are 0 (rows and columns are 0-indexed).
# 
# 
# Example 1:
# 
# 
# Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
# Output: 1
# Explanation: (1, 2) is a special position because mat[1][2] == 1 and all
# other elements in row 1 and column 2 are 0.
# 
# 
# Example 2:
# 
# 
# Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
# 
# 
# 
# Constraints:
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# mat[i][j] is either 0 or 1.
# 
# 
#
from typing import List 
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        m, n = len(mat), len(mat[0])
        row_sum = [0] * m
        col_sum = [0] * n
        for i in range(m):
            for j in range(n):
                row_sum[i] += mat[i][j]
                col_sum[j] += mat[i][j]
        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                    count += 1
        return count

# @lc code=end

