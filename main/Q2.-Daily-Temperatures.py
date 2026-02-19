1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        n = len(temperatures)
4        results = [0] * n
5        stack = []
6        for i in range(n):
7            while stack and temperatures[i] > temperatures[stack[-1]]:
8                idx = stack.pop()
9                results[idx] = i - idx
10            stack.append(i)
11        return results