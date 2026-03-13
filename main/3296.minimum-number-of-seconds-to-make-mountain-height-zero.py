#
# @lc app=leetcode id=3296 lang=python3
#
# [3296] Minimum Number of Seconds to Make Mountain Height Zero
#
# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/description/
#
# algorithms
# Medium (36.88%)
# Likes:    539
# Dislikes: 86
# Total Accepted:    91.5K
# Total Submissions: 158.5K
# Testcase Example:  '4\n[2,1,1]'
#
# You are given an integer mountainHeight denoting the height of a mountain.
# 
# You are also given an integer array workerTimes representing the work time of
# workers in seconds.
# 
# The workers work simultaneously to reduce the height of the mountain. For
# worker i:
# 
# 
# To decrease the mountain's height by x, it takes workerTimes[i] +
# workerTimes[i] * 2 + ... + workerTimes[i] * x seconds. For
# example:
# 
# 
# To reduce the height of the mountain by 1, it takes workerTimes[i]
# seconds.
# To reduce the height of the mountain by 2, it takes workerTimes[i] +
# workerTimes[i] * 2 seconds, and so on.
# 
# 
# 
# 
# Return an integer representing the minimum number of seconds required for the
# workers to make the height of the mountain 0.
# 
# 
# Example 1:
# 
# 
# Input: mountainHeight = 4, workerTimes = [2,1,1]
# 
# Output: 3
# 
# Explanation:
# 
# One way the height of the mountain can be reduced to 0 is:
# 
# 
# Worker 0 reduces the height by 1, taking workerTimes[0] = 2 seconds.
# Worker 1 reduces the height by 2, taking workerTimes[1] + workerTimes[1] * 2
# = 3 seconds.
# Worker 2 reduces the height by 1, taking workerTimes[2] = 1 second.
# 
# 
# Since they work simultaneously, the minimum time needed is max(2, 3, 1) = 3
# seconds.
# 
# 
# Example 2:
# 
# 
# Input: mountainHeight = 10, workerTimes = [3,2,2,4]
# 
# Output: 12
# 
# Explanation:
# 
# 
# Worker 0 reduces the height by 2, taking workerTimes[0] + workerTimes[0] * 2
# = 9 seconds.
# Worker 1 reduces the height by 3, taking workerTimes[1] + workerTimes[1] * 2
# + workerTimes[1] * 3 = 12 seconds.
# Worker 2 reduces the height by 3, taking workerTimes[2] + workerTimes[2] * 2
# + workerTimes[2] * 3 = 12 seconds.
# Worker 3 reduces the height by 2, taking workerTimes[3] + workerTimes[3] * 2
# = 12 seconds.
# 
# 
# The number of seconds needed is max(9, 12, 12, 12) = 12 seconds.
# 
# 
# Example 3:
# 
# 
# Input: mountainHeight = 5, workerTimes = [1]
# 
# Output: 15
# 
# Explanation:
# 
# There is only one worker in this example, so the answer is workerTimes[0] +
# workerTimes[0] * 2 + workerTimes[0] * 3 + workerTimes[0] * 4 + workerTimes[0]
# * 5 = 15.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= mountainHeight <= 10^5
# 1 <= workerTimes.length <= 10^4
# 1 <= workerTimes[i] <= 10^6
# 
# 
#

# @lc code=start

import math
from typing import List

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def can_reduce_in_time(time: int) -> bool:
            total = 0
            for wt in workerTimes:
                if time < wt:
                    continue
                # Quadratic formula: max x where wt * x * (x+1) / 2 <= time
                x = int((-1 + math.sqrt(1 + 8 * time / wt)) / 2)
                
                # Adjust for floating-point precision (at most ±1)
                if wt * (x + 1) * (x + 2) <= 2 * time:
                    x += 1
                elif wt * x * (x + 1) > 2 * time:
                    x -= 1
                
                total += max(0, x)
                if total >= mountainHeight:  # Early exit
                    return True
            return False
        
        # Binary search on answer
        # Upper bound: fastest worker does all work alone
        min_wt = min(workerTimes)
        lo, hi = 0, min_wt * mountainHeight * (mountainHeight + 1) // 2
        
        while lo < hi:
            mid = (lo + hi) // 2
            if can_reduce_in_time(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
# @lc code=end

