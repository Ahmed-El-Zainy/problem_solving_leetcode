#
# @lc app=leetcode id=3666 lang=python3
#
# [3666] Minimum Operations to Equalize Binary String
#

# @lc code=start
class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        
        def count_ops(target: str) -> int:
            arr = [int(c) for c in s]
            t = int(target)
            ops = 0
            flips = [0] * (n + 1)
            current_flips = 0
            
            for i in range(n):
                current_flips += flips[i]
                effective = (arr[i] + current_flips) % 2
                
                if effective != t:
                    if i + k > n:
                        return float('inf')
                    ops += 1
                    current_flips += 1
                    if i + k <= n:
                        flips[i + k] -= 1
            
            return ops
        
        r0 = count_ops('0')
        r1 = count_ops('1')
        
        best = min(r0, r1)
        return best if best != float('inf') else -1

# @lc code=end


