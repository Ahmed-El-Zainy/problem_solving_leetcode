#
# @lc app=leetcode id=1404 lang=python3
#
# [1404] Number of Steps to Reduce a Number in Binary Representation to One
#

# @lc code=start
class Solution:
    def numSteps(self, s: str) -> int:
        """
        The idea is to simulate the process of reducing the binary number to one.
        We can use a loop to repeatedly check the last bit of the binary string:
        - If the last bit is '0', we can simply divide the number by 2 (which is equivalent to removing the last bit).
        - If the last bit is '1', we need to add 1 to the number (which may cause a carry) and then divide by 2.
        We will keep track of the number of steps taken until we reduce the binary string to "1".
        """
        steps = 0
        while s != "1":
            if s[-1] == '0':
                s = s[:-1]  # Remove the last bit"""
            else:
                # Add 1 to the binary number
                s = bin(int(s, 2) + 1)[2:]  # Convert to int, add 1, convert back to binary
            steps += 1
        return steps
# @lc code=end

