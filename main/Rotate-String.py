1class Solution:
2    def rotateString(self, s: str, goal: str) -> bool:
3        if len(goal) != len(s):
4            return False
5        return goal in (s + s)