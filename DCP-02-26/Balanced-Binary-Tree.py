1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        def dfs(node: Optional[TreeNode]) -> Tuple[bool, int]:
10            if not node:
11                return True, 0
12            
13            left_balanced, left_height = dfs(node.left)
14            right_balanced, right_height = dfs(node.right)
15            
16            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
17            height = max(left_height, right_height) + 1
18            
19            return balanced, height
20        
21        balanced, _ = dfs(root)
22        return balanced
23