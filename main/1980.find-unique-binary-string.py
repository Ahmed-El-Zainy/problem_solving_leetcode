#
# @lc app=leetcode id=1980 lang=python3
#
# [1980] Find Unique Binary String
#
# https://leetcode.com/problems/find-unique-binary-string/description/
#
# algorithms
# Medium (79.44%)
# Likes:    2570
# Dislikes: 89
# Total Accepted:    304.8K
# Total Submissions: 383.3K
# Testcase Example:  '["01","10"]'
#
# Given an array of strings nums containing n unique binary strings each of
# length n, return a binary string of length n that does not appear in nums. If
# there are multiple answers, you may return any of them.
# 
# 
# Example 1:
# 
# 
# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.
# 
# 
# Example 2:
# 
# 
# Input: nums = ["00","01"]
# Output: "11"
# Explanation: "11" does not appear in nums. "10" would also be correct.
# 
# 
# Example 3:
# 
# 
# Input: nums = ["111","011","001"]
# Output: "101"
# Explanation: "101" does not appear in nums. "000", "010", "100", and "110"
# would also be correct.
# 
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 16
# nums[i].length == n
# nums[i] is either '0' or '1'.
# All the strings of nums are unique.
# 
# 
#

# @lc code=start
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums)
        ans = []
        for i in range(n):
            ans.append('1' if nums[i][i] == '0' else '0')
        return ''.join(ans)
# @lc code=end

