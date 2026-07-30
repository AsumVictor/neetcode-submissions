# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        if node is not there: return true

        a  right node should be greater than the parent
        a left node should be less than the parent

        for every node:

            if node is grater min_val: False

            if a node is less than max_val: false


            1 less than 2
            3 should be less than 2

            min, max
            max, min

        
        right: min--> right > min
        left: max--> left < max

        i

        """

        def dfs(node, max_val, min_val):

            if not node:
                return True

            
            if node.val <= min_val or node.val >= max_val:
                return False

            
            left = dfs(node.left, node.val, min_val)
            right = dfs(node.right, max_val, node.val)

            return left and right

        
        return dfs(root, float("inf"), float("-inf"))

