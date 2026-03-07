#
# @lc app=leetcode id=1888 lang=python3
#
# [1888] Minimum Number of Flips to Make the Binary String Alternating
#
# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/description/
#
# algorithms
# Medium (41.06%)
# Likes:    1301
# Dislikes: 86
# Total Accepted:    37K
# Total Submissions: 89.8K
# Testcase Example:  '"111000"'
#
# You are given a binary string s. You are allowed to perform two types of
# operations on the string in any sequence:
# 
# 
# Type-1: Remove the character at the start of the string s and append it to
# the end of the string.
# Type-2: Pick any character in s and flip its value, i.e., if its value is '0'
# it becomes '1' and vice-versa.
# 
# 
# Return the minimum number of type-2 operations you need to perform such that
# s becomes alternating.
# 
# The string is called alternating if no two adjacent characters are
# equal.
# 
# 
# For example, the strings "010" and "1010" are alternating, while the string
# "0100" is not.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "111000"
# Output: 2
# Explanation: Use the first operation two times to make s = "100011".
# Then, use the second operation on the third and sixth elements to make s =
# "101010".
# 
# 
# Example 2:
# 
# 
# Input: s = "010"
# Output: 0
# Explanation: The string is already alternating.
# 
# 
# Example 3:
# 
# 
# Input: s = "1110"
# Output: 1
# Explanation: Use the second operation on the second element to make s =
# "1010".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s[i] is either '0' or '1'.
# 
# 
#

# @lc code=start
class Solution:
    def minFlips(self, s: str) -> int:
        
        n = len(s)
        s += s
        alt1 = ''.join('0' if i % 2 == 0 else '1' for i in range(2 * n))
        alt2 = ''.join('1' if i % 2 == 0 else '0' for i in range(2 * n))

        diff1 = sum(1 for i in range(n) if s[i] != alt1[i])
        diff2 = sum(1 for i in range(n) if s[i] != alt2[i])

        ans = min(diff1, diff2)

        for i in range(n, 2 * n):
            if s[i] != alt1[i]:
                diff1 += 1
            if s[i - n] != alt1[i - n]:
                diff1 -= 1

            if s[i] != alt2[i]:
                diff2 += 1
            if s[i - n] != alt2[i - n]:
                diff2 -= 1

            ans = min(ans, diff1, diff2)

        return ans
# @lc code=end

