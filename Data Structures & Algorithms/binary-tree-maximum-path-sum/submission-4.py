# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        for every node:
            get max path from left and right

            set max to be the left + node, right + node, node, and left + right + node

            now return max of left, right, node, left+node, right + node
        """
        self.res = float("-inf")
        def dfs(node):

            if not node:
                return float("-inf")

            left = dfs(node.left)
            right = dfs(node.right)

            self.res = max(
                        self.res, 
                        left + node.val,
                        right + node.val,
                        node.val,
                        left + node.val + right
                        )
            
            return max(left + node.val, right + node.val, node.val)

        
        dfs(root)
        return self.res

