# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
         * Keep track of running path and path from node

         we return when reach a new leaf node

         if we reach a node:

             check the max path from the parent node.
             check the max path from the node as root node

        """
        self.over_all = float("-inf")
        def dfs(node, height):

            if not node:
                return height - 1
            

            left = dfs(node.left, 1)
            right = dfs(node.right, 1)

            diameter = left + right

            self.over_all = max(self.over_all, diameter)



            return height + max(left, right)
        

        
        dfs(root, 0)
        
        return self.over_all







