1class Solution:
2    def earliestTime(self, tasks: List[List[int]]) -> int:
3        """
4        time complexity : O(1)
5        """
6        return min([x + y for x, y in tasks])