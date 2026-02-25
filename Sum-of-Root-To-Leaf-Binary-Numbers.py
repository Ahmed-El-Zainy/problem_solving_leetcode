1class Solution:
2    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
3        
4        def dfs(node, path):
5            if not node:
6                return 0
7            
8            path += str(node.val)
9            if not node.left and not node.right:
10                return int(path, 2)
11            return dfs(node.left, path) + dfs(node.right, path)
12        
13        return dfs(root, "")