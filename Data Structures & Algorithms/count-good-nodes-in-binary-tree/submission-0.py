# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        
        def dfs(node, max_val):
            
            if node is None:
                return 0

            num_of_good_node = 0
            if node.val >= max_val:
                num_of_good_node += 1
                max_val = node.val
            
            num_of_good_node += dfs(node.left, max_val)
            num_of_good_node += dfs(node.right, max_val)

            return num_of_good_node

        
        return dfs(root, float("-inf"))



        