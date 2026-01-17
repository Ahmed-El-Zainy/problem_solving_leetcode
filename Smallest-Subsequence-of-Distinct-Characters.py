1class Solution:
2    def smallestSubsequence(self, s: str) -> str:
3        last = {c:i for i, c in enumerate(s)}
4        stack = []
5        seen = set()
6        for i, c in enumerate(s):
7            if c not in seen:
8                # while stack and c < stack[-1] and i < last[stack[-1]]:
9                while stack and c < stack[-1] and i < last[stack[-1]]:
10                    seen.remove(stack.pop())
11                stack.append(c)
12                seen.add(c)
13        return "".join(stack)
14