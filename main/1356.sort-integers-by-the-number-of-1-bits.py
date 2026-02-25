#
# @lc app=leetcode id=1356 lang=python3
#
# [1356] Sort Integers by The Number of 1 Bits
#

# @lc code=start
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        def count_ones(n):
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count
        
        arr.sort(key=lambda x: (count_ones(x), x))
        return arr
# @lc code=end

