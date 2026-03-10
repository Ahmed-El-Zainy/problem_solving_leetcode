#
# @lc app=leetcode id=3130 lang=python3
#
# [3130] Find All Possible Stable Binary Arrays II
#
# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/description/
#
# algorithms
# Hard (27.27%)
# Likes:    89
# Dislikes: 14
# Total Accepted:    6.5K
# Total Submissions: 19.4K
# Testcase Example:  '1\n1\n2'
#
# You are given 3 positive integers zero, one, and limit.
# 
# A binary array arr is called stable if:
# 
# 
# The number of occurrences of 0 in arr is exactly zero.
# The number of occurrences of 1 in arr is exactly one.
# Each subarray of arr with a size greater than limit must contain both 0 and
# 1.
# 
# 
# Return the total number of stable binary arrays.
# 
# Since the answer may be very large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: zero = 1, one = 1, limit = 2
# 
# Output: 2
# 
# Explanation:
# 
# The two possible stable binary arrays are [1,0] and [0,1].
# 
# 
# Example 2:
# 
# 
# Input: zero = 1, one = 2, limit = 1
# 
# Output: 1
# 
# Explanation:
# 
# The only possible stable binary array is [1,0,1].
# 
# 
# Example 3:
# 
# 
# Input: zero = 3, one = 3, limit = 2
# 
# Output: 14
# 
# Explanation:
# 
# All the possible stable binary arrays are [0,0,1,0,1,1], [0,0,1,1,0,1],
# [0,1,0,0,1,1], [0,1,0,1,0,1], [0,1,0,1,1,0], [0,1,1,0,0,1], [0,1,1,0,1,0],
# [1,0,0,1,0,1], [1,0,0,1,1,0], [1,0,1,0,0,1], [1,0,1,0,1,0], [1,0,1,1,0,0],
# [1,1,0,0,1,0], and [1,1,0,1,0,0].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= zero, one, limit <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j][k]: ways to place i zeros and j ones, last element is k
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # Base cases: arrays of all 0s or all 1s (length <= limit)
        for i in range(1, min(limit, zero) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(limit, one) + 1):
            dp[0][j][1] = 1
        
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # Place a 0 at the end
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD
                # Subtract invalid: run of (limit+1) zeros
                # That means before these limit zeros there was a 1 (or nothing)
                if i >= limit + 1:
                    dp[i][j][0] -= dp[i-limit-1][j][1]
                    if i == limit + 1 and j == 0:
                        dp[i][j][0] -= 1  # pure zeros array of length limit+1
                
                # Place a 1 at the end
                dp[i][j][1] = (dp[i][j-1][0] + dp[i][j-1][1]) % MOD
                # Subtract invalid: run of (limit+1) ones
                if j >= limit + 1:
                    dp[i][j][1] -= dp[i][j-limit-1][0]
                    if j == limit + 1 and i == 0:
                        dp[i][j][1] -= 1
                
                dp[i][j][0] %= MOD
                dp[i][j][1] %= MOD
        
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD


# @lc code=end

