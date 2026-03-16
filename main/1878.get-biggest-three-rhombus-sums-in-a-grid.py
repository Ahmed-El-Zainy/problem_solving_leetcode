#
# @lc app=leetcode id=1878 lang=python3
#
# [1878] Get Biggest Three Rhombus Sums in a Grid
#
# https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/description/
#
# algorithms
# Medium (50.09%)
# Likes:    455
# Dislikes: 593
# Total Accepted:    81.4K
# Total Submissions: 114.7K
# Testcase Example:  '[[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]'
#
# You are given an m x n integer matrix grid​​​.
# 
# A rhombus sum is the sum of the elements that form the border of a regular
# rhombus shape in grid​​​. The rhombus must have the shape of a square rotated
# 45 degrees with each of the corners centered in a grid cell. Below is an
# image of four valid rhombus shapes with the corresponding colored cells that
# should be included in each rhombus sum:
# 
# Note that the rhombus can have an area of 0, which is depicted by the purple
# rhombus in the bottom right corner.
# 
# Return the biggest three distinct rhombus sums in the grid in descending
# order. If there are less than three distinct values, return all of them.
# 
# 
# Example 1:
# 
# 
# Input: grid =
# [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
# Output: [228,216,211]
# Explanation: The rhombus shapes for the three biggest distinct rhombus sums
# are depicted above.
# - Blue: 20 + 3 + 200 + 5 = 228
# - Red: 200 + 2 + 10 + 4 = 216
# - Green: 5 + 200 + 4 + 2 = 211
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [20,9,8]
# Explanation: The rhombus shapes for the three biggest distinct rhombus sums
# are depicted above.
# - Blue: 4 + 2 + 6 + 8 = 20
# - Red: 9 (area 0 rhombus in the bottom right corner)
# - Green: 8 (area 0 rhombus in the bottom middle)
# 
# 
# Example 3:
# 
# 
# Input: grid = [[7,7,7]]
# Output: [7]
# Explanation: All three possible rhombus sums are the same, so return [7].
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j] <= 10^5
# 
# 
#
from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set()
        
        def get_rhombus_sum(i: int, j: int, k: int) -> int:
            """حساب مجموع حدود معين رأسه العلوي عند (i,j) وطول ضلعه k"""
            if k == 0:
                return grid[i][j]
            
            # التأكد من أن المعين داخل حدود الشبكة
            if i + 2*k >= m or j - k < 0 or j + k >= n:
                return -1
            
            total = 0
            # الضلع الأول: من الأعلى لليمين ↘
            for d in range(k):
                total += grid[i + d][j + d]
            # الضلع الثاني: من اليمين للأسفل ↙
            for d in range(k):
                total += grid[i + k + d][j + k - d]
            # الضلع الثالث: من الأسفل لليسار ↖
            for d in range(k):
                total += grid[i + 2*k - d][j - d]
            # الضلع الرابع: من اليسار للأعلى ↗
            for d in range(k):
                total += grid[i + k - d][j - k + d]
            
            return total
        
        # تجربة كل موضع ممكن كرأس علوي للمعين
        for i in range(m):
            for j in range(n):
                # أقصى حجم للمعين من هذا الموضع
                max_k = min((m - 1 - i) // 2, j, n - 1 - j)
                for k in range(max_k + 1):
                    s = get_rhombus_sum(i, j, k)
                    if s != -1:
                        sums.add(s)
        
        # إرجاع أكبر 3 قيم مميزة
        return sorted(sums, reverse=True)[:3]