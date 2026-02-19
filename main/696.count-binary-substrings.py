#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0
        count = 1
        result = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                result += min(prev, count)
                prev = count
                count = 1
        result += min(prev, count)
        return result



# @lc code=end

