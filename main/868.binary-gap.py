#
# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        
        # Convert n to binary string
        binary_str = bin(n)[2:]  # Remove '0b' prefix
        
        max_gap = 0
        last_one_index = None
        
        for i, bit in enumerate(binary_str):
            if bit == '1':
                if last_one_index is not None:
                    gap = i - last_one_index
                    max_gap = max(max_gap, gap)
                last_one_index = i
        
        return max_gap
# @lc code=end

