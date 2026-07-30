# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        """
            2
          /   \
        3      4
       / \     \
       3  3     2
                \ 
                5

    
      - for we interchange the keft and right of a node

      # check if the node is a left node that is if no left and right

      # swap the child nodes

        """
        def invert(node):
            if not node:
                return

            leftNode = node.left
            node.left = node.right
            node.right = leftNode
            invert(node.left)
            invert(node.right)

            return

        invert(root)
        
        return root

