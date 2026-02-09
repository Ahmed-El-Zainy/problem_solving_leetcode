1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        result = []
10        def dfs(node):
11            if not node:
12                return
13            dfs(node.left)
14            result.append(node.val)
15            dfs(node.right)
16        dfs(root)
17        def build(l, r):
18            if l > r:
19                return None
20            mid = (l + r) // 2
21            node = TreeNode(result[mid])
22            node.left = build(l, mid - 1)
23            node.right = build(mid + 1, r)
24            return node
25        
26        return build(0, len(result) - 1)