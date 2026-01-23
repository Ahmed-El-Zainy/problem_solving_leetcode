1
2class Solution:
3    def rotateString(self, s: str, goal: str) -> bool:
4        if len(s) != len(goal):
5            return False
6        return goal in (s + s)