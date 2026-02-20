#
# @lc app=leetcode id=761 lang=python3
#
# [761] Special Binary String
#



# @lc code=start
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # A special binary string:
        # 1. Equal number of 0s and 1s
        # 2. Every prefix has >= as many 1s as 0s
        # (Same structure as valid parentheses: 1='(' 0=')')
        
        # Strategy: Find top-level special substrings, recursively
        # sort their insides, then sort them in descending order
        
        count = 0
        start = 0
        specials = []
        
        for i, ch in enumerate(s):
            if ch == '1':
                count += 1
            else:
                count -= 1
            
            if count == 0:
                # s[start:i+1] is a top-level special string
                # Recursively optimize the inside (strip outer 1 and 0)
                inner = self.makeLargestSpecial(s[start+1:i])
                specials.append('1' + inner + '0')
                start = i + 1
        
        # Sort descending so largest special strings come first
        specials.sort(reverse=True)
        return ''.join(specials)



# @lc code=end

