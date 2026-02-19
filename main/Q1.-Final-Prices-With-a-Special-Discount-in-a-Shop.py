1class Solution:
2    def finalPrices(self, prices: List[int]) -> List[int]:
3        stack = []
4        n = len(prices)
5        results = prices[:]
6        for i in range(n):
7            while  stack  and prices[stack[-1]] >= prices[i]:
8                idx = stack.pop()
9                results[idx] -= prices[i]
10            stack.append(i)
11        return results
12
13